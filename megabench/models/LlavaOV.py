import logging
from PIL import Image, ImageFile
from mimetypes import guess_type
from tqdm import tqdm
import pathlib
import torch
import json
import copy
import warnings
import re
from models.OpenAI import OpenAI
from llava.model.builder import load_pretrained_model
from llava.mm_utils import (
    process_images,
    tokenizer_image_token,
)
from llava.constants import (
    IMAGE_TOKEN_INDEX,
    DEFAULT_IMAGE_TOKEN,
)
from llava.conversation import conv_templates

warnings.filterwarnings("ignore")
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
ImageFile.LOAD_TRUNCATED_IMAGES = True

logger = logging.getLogger("infoLogger")


class LlavaOV(OpenAI):
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

        llava_model_args = {
            "multimodal": True,
        }
        overwrite_config = {}
        overwrite_config["image_aspect_ratio"] = "pad"
        llava_model_args["overwrite_config"] = overwrite_config
        self.tokenizer, self.model, self.image_processor, self.max_length = (
            load_pretrained_model(
                model, None, "llava_qwen", device_map="auto", **llava_model_args
            )
        )

        self.model.eval()

    @staticmethod
    def load_config(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def create_image_content(self, image_path):
        image, mime_type = self.encode_image(image_path)
        return image

    def encode_image(self, image_path, max_side=None):
        mime_type, _ = guess_type(image_path)
        if mime_type is None:
            mime_type = "image/jpeg"

        image = Image.open(image_path)
        # Handle the alpha channel
        if image.mode == "RGBA":
            image = self._rgba_to_rgb(image)

        # if not specified, using the
        if not max_side and self.max_side:
            max_side = self.max_side

        if self.resize and max(image.size) > self.max_side:
            image = self._resize_image(image)

        return image.convert("RGB"), mime_type

    def create_media_content(self, file_path, is_demo=False):
        if self._is_video_file(file_path):
            # Handle video processing with the frame subsampling logic
            return self.process_video(file_path, is_demo)
        else:
            # Handle image processing otherwise
            return [self.create_image_content(file_path)]

    def _process_text_and_media(self, text, media_paths, is_example=False):
        content = []
        images = []
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
            if chunk == "<image>":
                if is_example and curr_demo_images >= self.max_demo_num_image:
                    logging.warning(
                        "Exceed the quota for demo image, skip the demo image"
                    )
                else:
                    image_content = self.create_media_content(
                        media_paths[media_index], is_demo=is_example
                    )
                    content.append(DEFAULT_IMAGE_TOKEN)
                    images.extend(image_content)
                    if is_example:
                        curr_demo_images += 1
                media_index += 1
            elif chunk == "<video>":
                video_content = self.create_media_content(
                    media_paths[media_index], is_demo=is_example
                )
                content.append(self.prompts["video_start"])
                for _ in video_content:
                    content.append(DEFAULT_IMAGE_TOKEN)
                content.append(self.prompts["video_end"])
                images.extend(video_content)
                media_index += 1
            elif chunk.strip():  # Only add non-empty text chunks
                content.append(chunk.strip())

        return content, images

    def prepare_context(self):
        content, images = [], []
        global_description = self.query_data.get("global_description", "")
        global_image_paths = self.query_data.get("global_images", [])

        context_content, context_images = self._process_text_and_media(
            global_description, global_image_paths
        )
        content.extend(context_content)
        images.extend(context_images)

        example_info = self.query_data["example_info"]
        example_content, example_images = self.prepare_example_content(example_info)
        content.extend(example_content)
        images.extend(example_images)

        return content, images

    def prepare_example_content(self, example_info):
        example_text = example_info["example_text"]
        example_media_paths = example_info["image_paths"]
        example_content, example_images = self._process_text_and_media(
            example_text, example_media_paths, is_example=True
        )

        return example_content, example_images

    def prepare_query_content(self, query_info):
        query_text = query_info.get("query_text", "")
        image_paths = query_info.get("image_paths", [])
        query_content, query_images = self._process_text_and_media(
            query_text, image_paths
        )

        return query_content, query_images

    def query(self, task_name, query_data, position=0):
        self.query_data = query_data

        self._set_sampling_config(0)
        context, context_image_list = self.prepare_context()
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
                images = []
                images.extend(context_image_list)

                query_content, query_images_list = self.prepare_query_content(
                    query_info
                )

                if query_images_list:
                    images.extend(query_images_list)

                image_tensors = process_images(
                    images, self.image_processor, self.model.config
                )

                device = "cuda:0" if not hasattr(self, "device") else self.device
                image_tensors = [
                    _image.to(dtype=torch.float16, device=device)
                    for _image in image_tensors
                ]

                conv_template = "qwen_1_5"
                query_payload_list = context + query_content
                query_payload = "\n".join(query_payload_list)

                if self.print_response:
                    print("Query information:", query_payload)
                conv = copy.deepcopy(conv_templates[conv_template])
                conv.append_message(conv.roles[0], query_payload)
                conv.append_message(conv.roles[1], None)
                prompt_question = conv.get_prompt()
                input_ids = tokenizer_image_token(
                    prompt_question,
                    self.tokenizer,
                    IMAGE_TOKEN_INDEX,
                    return_tensors="pt",
                ).unsqueeze(0)
                if hasattr(self, "device"):
                    input_ids = input_ids.to(self.device)
                else:
                    input_ids = input_ids.to("cuda:0")
                image_sizes = [image.size for image in images]

                max_new_tokens = self.config.get("session_len", 8192)

                import signal

                def handler(signum, frame):
                    raise TimeoutError("Function call timed out")

                timeout = self.config.get("timeout", 60)
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(timeout)

                try:
                    cont = self.model.generate(
                        input_ids,
                        images=image_tensors,
                        image_sizes=image_sizes,
                        do_sample=False,
                        temperature=0,
                        max_new_tokens=max_new_tokens,
                    )
                    text_outputs = self.tokenizer.batch_decode(
                        cont, skip_special_tokens=True
                    )
                    text_outputs = text_outputs[0]
                except TimeoutError as e:
                    text_outputs = str(e)
                finally:
                    signal.alarm(0)
            else:
                text_outputs = (
                    "Exceed the specified max number of images, skip running the model."
                )

            if self.print_response:
                print("Model response:", text_outputs)
            query_response.append(
                {
                    "response": text_outputs,
                    "correct_answer": query_info["query_answer"],
                }
            )
        return query_response
