import base64
import requests
import logging
import json
from models.openai import OpenAI
from PIL import Image, ImageFile
from io import BytesIO
from mimetypes import guess_type
from tqdm import tqdm
from transformers import AutoProcessor, Gemma3ForConditionalGeneration
import torch
import pathlib


class Gemma(OpenAI):

    def __init__(
        self,
        api_key=None,
        model=None,
        query_data=None,
        resize=True,
        max_side=1000,
        print_response=False,
        max_num_image=None,
        system_message=None,
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
        # load config from config.json
        self.config = self.load_config(
            pathlib.Path(__file__).resolve().parent / "config.json"
        )
        self.model = Gemma3ForConditionalGeneration.from_pretrained(
            model, device_map="auto"
        ).eval()
        self.processor = AutoProcessor.from_pretrained(model)
        
        
    @staticmethod
    def load_config(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
        
    def prepare_system_message(self):
        return [{
        "role": "system",
        "content": [{"type": "text", "text": "You are a helpful assistant."}]
    }]

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
            "image": f"{base64_image}",
            # "image": {"url": f"data:{mime_type};base64,{base64_image}"},
        }

    def encode_image(self, image_path, max_side=None):
        mime_type, _ = guess_type(image_path)
        if mime_type is None:
            mime_type = "image/jpeg"
        image_format = mime_type.split("/")[-1].upper() if mime_type else "JPEG"

        image = Image.open(image_path)
        # Handle the alpha channel
        if image.mode == "RGBA":
            image = self._rgba_to_rgb(image)
        if not max_side and self.max_side:
            max_side = self.max_side

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
            query_content = self.prepare_query_content(query_info)

            if not exceed_image_quota:
                messages = self.prepare_system_message()
                messages.append({"role": "user", "content": context + query_content})
                inputs = self.processor.apply_chat_template(
                    messages, add_generation_prompt=True, tokenize=True,
                    return_dict=True, return_tensors="pt"
                ).to(self.model.device, dtype=torch.bfloat16)
                input_len = inputs["input_ids"].shape[-1]
                
                import signal
                def handler(signum, frame):
                    raise TimeoutError("Function call timed out")

                timeout = self.config.get("timeout", 180)
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(timeout)

                try:
                    with torch.inference_mode():
                        generation = self.model.generate(**inputs, max_new_tokens=4096, do_sample=False)
                        generation = generation[0][input_len:]

                    response = self.processor.decode(generation, skip_special_tokens=True)
                    print(response)
                    message_content = response
                except TimeoutError as e:
                    message_content = str(e)
                finally:
                    signal.alarm(0)
            else:
                message_content = (
                    "Exceed the specified max number of images, skip..."
                )

            # save the correct answer here as well for later scoring
            query_response.append(
                {
                    "response": message_content,
                    "correct_answer": query_info["correct_answer"],
                }
            )

        return query_response

