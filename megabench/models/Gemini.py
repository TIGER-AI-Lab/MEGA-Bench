import os
from PIL import Image
import tempfile
import time
import math
import ssl
from tqdm import tqdm
import logging
import re
from models.base_model import BaseModel
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from google.api_core.exceptions import (
    ServiceUnavailable,
    PermissionDenied,
    ResourceExhausted,
    InternalServerError,
)
from googleapiclient.errors import HttpError


class Gemini(BaseModel):

    def __init__(
        self,
        api_key=None,
        model=None,
        query_data=None,
        resize=True,
        max_side=1000,
        print_response=True,
        max_num_image=None,
        system_message: str | None = None,
        total_demo_video_frames=4,
        **kwargs,
    ):
        super().__init__(
            api_key,
            model,
            query_data,
            resize,
            max_side,
            print_response,
            max_num_image,
            system_message,
            total_demo_video_frames,
            **kwargs,
        )

        self.current_key_index = 0
        self.ERROR_THRESHOLD = 5
        self.REJ_THRESHOLD = 3

    def create_media_content(self, file_path, is_demo=False):
        if self._is_video_file(file_path):
            # Handle video processing with the frame subsampling logic
            video_content = [self.prompts["video_start"]]
            video_content.extend(self.process_video(file_path, is_demo))
            video_content.append(self.prompts["video_end"])
            return video_content
        else:
            # Handle image processing otherwise
            return [self.create_image_content(file_path)]

    def create_image_content(self, image_path):
        max_retries = 5
        for attempt in range(max_retries):
            try:
                image = Image.open(image_path)
                if image.mode == "RGBA":
                    image = self._rgba_to_rgb(image)
                temp_file = self._resize_and_save_temp_image(image)
                image = genai.upload_file(temp_file)
                os.remove(
                    temp_file
                )  # clean up the temp file once the image is uploaded
                return image
            except (
                TimeoutError,
                ssl.SSLError,
                ServiceUnavailable,
                PermissionDenied,
                HttpError,
            ) as exc:
                if attempt < max_retries - 1:
                    logging.info(
                        f"File upload failed({type(exc).__name__}), retry {attempt + 1}/{max_retries}..."
                    )
                    time.sleep(2)
                else:
                    raise exc

    def _resize_and_save_temp_image(self, image):
        if self.resize and max(image.size) > self.max_side:
            image = self._resize_image(image)
        temp_image = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        image.save(temp_image, format="PNG")
        temp_image.close()
        return temp_image.name

    def _process_text_and_media(self, text, media_paths, is_example=False):
        content = []
        chunks = re.split(r"(<image>|<video>)", text)

        placeholder_count = sum(
            1 for chunk in chunks if chunk in ["<image>", "<video>"]
        )

        if placeholder_count != len(media_paths):
            raise ValueError(
                f"Mismatch between number of placeholders ({placeholder_count}) and media paths ({len(media_paths)})"
            )

        media_index = 0
        curr_demo_images = 0
        for chunk in chunks:
            if chunk in ["<image>", "<video>"]:
                media_content = self.create_media_content(
                    media_paths[media_index], is_demo=is_example
                )
                if len(media_content) == 1:  # image
                    if is_example and curr_demo_images >= self.max_demo_num_image:
                        logging.warning(
                            "Exceed the quota for demo image, skip the demo image"
                        )
                    else:
                        content.extend(media_content)
                        if is_example:
                            curr_demo_images += 1
                else:  # video
                    content.extend(media_content)
                media_index += 1
            elif chunk.strip():  # Only add non-empty text chunks
                content.append(chunk.strip())

        return content

    def prepare_context(self):
        global_description = self.query_data.get("global_description", "")
        global_images = self.query_data.get("global_images", [])
        content = self._process_text_and_media(global_description, global_images)

        example_info = self.query_data["example_info"]
        example_content = self.prepare_example_content(example_info)
        content.extend(example_content)

        return content

    def prepare_example_content(self, example_info):
        example_text = example_info["example_text"]
        example_media_paths = example_info["image_paths"]
        return self._process_text_and_media(
            example_text, example_media_paths, is_example=True
        )

    def prepare_query_content(self, query_info):
        query_text = query_info.get("query_text", "")
        image_paths = query_info.get("image_paths", [])
        query_content = self._process_text_and_media(query_text, image_paths)
        return query_content

    def _prepare_data_with_lower_rate(self, query_info, query_idx, rate):
        _save = (
            self.max_num_image,
            self.total_demo_video_frames,
            self.max_demo_num_image,
        )
        self.max_num_image = math.floor(self.max_num_image / rate)
        self.total_demo_video_frames = math.floor(self.total_demo_video_frames / rate)
        self.max_demo_num_image = math.floor(self.max_demo_num_image / rate)
        self._set_sampling_config(query_idx)
        content = self.prepare_context()
        query_content = self.prepare_query_content(query_info)
        # recover the origial values
        self.max_num_image, self.total_demo_video_frames, self.max_demo_num_image = (
            _save
        )
        return content, query_content

    def query(self, task_name, query_data, position=0):
        self.query_data = query_data
        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(
            model_name=self.model,
            generation_config=genai.GenerationConfig(
                temperature=0,
            ),
            system_instruction=self.system_message,
        )

        self._set_sampling_config(0)
        context = self.prepare_context()

        query_response = []

        for query_idx, query_info in enumerate(
            tqdm(
                query_data["queries"],
                desc=f"{task_name} - Processing queries",
                unit="query",
                position=position,
                mininterval=0.1,
                miniters=1,
            )
        ):
            exceed_image_quota = self._set_sampling_config(query_idx)

            if not exceed_image_quota:
                query_content = self.prepare_query_content(query_info)
                response_data = None
                attempt = 0
                retrieve_attempt = 0
                context_ = context  # avoid changing the context for later queries
                while not response_data:
                    try:
                        response = model.generate_content(
                            context_ + query_content,
                            safety_settings={
                                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                            },
                        )
                        response_data = response.text
                    except ValueError as e:
                        # Query rejected by the API
                        logging.info(f"Failed to retrieve response text: {e}")
                        logging.info(f"Response details: {response}")
                        logging.info(f"Retry {retrieve_attempt + 1}...")
                        time.sleep(3)
                        retrieve_attempt += 1
                        context_, query_content = self._prepare_data_with_lower_rate(
                            query_info,
                            query_idx,
                            1 + retrieve_attempt / self.REJ_THRESHOLD,
                        )
                        if retrieve_attempt > self.REJ_THRESHOLD:
                            response_data = f"API Blocked: {e}"
                    except (ResourceExhausted, InternalServerError) as exc:
                        logging.info(f"API exceptions: {exc}...")
                        logging.info(f"Retry {attempt + 1}...")
                        wait_time = min(2**attempt, 32)
                        time.sleep(wait_time)
                        attempt += 1
                        if attempt > self.ERROR_THRESHOLD:
                            response_data = (
                                f"API quota exceeded, recheck the results: {exec}"
                            )
            else:
                response_data = (
                    "Exceed the specified max number of images, skip running the model."
                )

            if self.print_response:
                logging.info("response " + str(query_idx) + ": " + response_data)
            query_response.append(
                {
                    "response": response_data,
                    "correct_answer": query_info["correct_answer"],
                }
            )

        return query_response
