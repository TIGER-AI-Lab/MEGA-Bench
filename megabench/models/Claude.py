import base64
from PIL import Image
from io import BytesIO
import anthropic
from models.base_model import BaseModel
from mimetypes import guess_type
import time
import logging
from tqdm import tqdm
from anthropic.types import message
from anthropic import InternalServerError, BadRequestError


class Claude(BaseModel):

    ATTEMPT_LIMIT = 5

    def create_media_content(self, file_path, is_demo=False):
        if self._is_video_file(file_path):
            # Handle video processing with the frame subsampling logic
            video_content = [{"type": "text", "text": self.prompts["video_start"]}]
            video_content.extend(self.process_video(file_path, is_demo))
            video_content.append({"type": "text", "text": self.prompts["video_end"]})
            return video_content
        else:
            # Handle image processing otherwise
            return [self.create_image_content(file_path)]

    def create_image_content(self, image_path):
        base64_image, mime_type = self.encode_image(image_path)
        return {
            "type": "image",
            "source": {"media_type": mime_type, "type": "base64", "data": base64_image},
        }

    def encode_image(self, image_path):
        mime_type, _ = guess_type(image_path)
        if mime_type is None:
            mime_type = "image/jpeg"
        image_format = mime_type.split("/")[-1].upper() if mime_type else "JPEG"

        image = Image.open(image_path)
        if image.mode == "RGBA":
            image = self._rgba_to_rgb(image)
        if self.resize and max(image.size) > self.max_side:
            image = self._resize_image(image)
        encoded_image = self._encode_image(image, image_format)

        return encoded_image, mime_type

    def _encode_image(self, image, image_format):
        with BytesIO() as output:
            image.convert("RGB").save(output, format=image_format)
            base64_encoded_data = base64.b64encode(output.getvalue()).decode("utf-8")
        return base64_encoded_data

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
        return self._process_text_and_media(example_text, example_media_paths, is_example=True)

    def prepare_query_content(self, query_info):
        query_text = query_info.get("query_text", "")
        image_paths = query_info.get("image_paths", [])
        query_content = self._process_text_and_media(query_text, image_paths)
        return query_content

    def query(self, task_name, query_data, position=0):
        self.query_data = query_data
        client = anthropic.Anthropic(api_key=self.api_key, max_retries=5)

        self._set_sampling_config(0)
        context = self.prepare_context()

        query_response = []

        for query_idx, query_info in enumerate(
            tqdm(
                query_data["queries"],
                desc=f"{task_name} - Processing queries",
                unit="query",
                position=position,
            )
        ):
            exceed_image_quota = self._set_sampling_config(query_idx)

            if not exceed_image_quota:
                query_content = self.prepare_query_content(query_info)

                messages = self.prepare_system_message()
                messages.append({"role": "user", "content": context + query_content})

                response = None
                n_attempt = 0
                while response is None:
                    try:
                        response: anthropic.types.Message = client.messages.create(
                            model=self.model,
                            temperature=0,
                            max_tokens=4096,
                            messages=messages,
                        )
                        time.sleep(1)
                    except (BadRequestError, InternalServerError) as e:
                        n_attempt += 1
                        logging.info(
                            f"Got error: {e}. Retry... Attemp times: {n_attempt}"
                        )
                        time.sleep(2)
                        if n_attempt >= self.ATTEMPT_LIMIT:
                            response = str(e)

                if isinstance(response, message.Message):
                    text_content = response.content[0].text
                    input_tokens = response.usage.input_tokens
                    output_tokens = response.usage.output_tokens
                else:
                    text_content = response
                    input_tokens = output_tokens = "NA"

                if self.print_response:
                    logging.info(
                        f"response: {text_content} ; tokens: {input_tokens + output_tokens}"
                    )

            else:
                text_content = (
                    "Exceed the specified max number of images, skip running the model."
                )
                logging.info(text_content)

            query_response.append(
                {
                    "response": text_content,
                    "correct_answer": query_info["correct_answer"],
                }
            )

        return query_response
