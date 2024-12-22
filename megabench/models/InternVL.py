import base64
import logging
from PIL import Image, ImageFile
from io import BytesIO
from tqdm import tqdm
import pathlib
import json
from models.OpenAI import OpenAI
from PIL import Image
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams
import re


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
ImageFile.LOAD_TRUNCATED_IMAGES = True


class InternVL(OpenAI):
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
        self.tokenizer = AutoTokenizer.from_pretrained(model, trust_remote_code=True)

        self.llm = LLM(
            model=model,
            max_num_seqs=8,
            max_model_len=8192,
            limit_mm_per_prompt={"image": max_num_image},
            trust_remote_code=True,
            tensor_parallel_size=kwargs.get("ngpus", 1),
            gpu_memory_utilization=kwargs.get("gpu_utils", 0.9)
        )

    @staticmethod
    def load_config(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def create_image_content(self, image_path):
        base64_image, mime_type = self.encode_image(image_path)
        image = Image.open(BytesIO(base64.b64decode(base64_image)))
        image.load()
        return image

    def create_media_content(self, file_path, is_demo=False):
        if self._is_video_file(file_path):
            # Handle video processing with the frame subsampling logic
            return self.process_video(file_path, is_demo)
        else:
            # Handle image processing otherwise
            return [self.create_image_content(file_path)]

    def prepare_context(self):
        content, images = [], []
        global_description = self.query_data.get("global_description", "")
        global_image_paths = self.query_data.get("global_images", [])
        
        context_content, context_images = self._process_text_and_media(global_description, global_image_paths)
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
        example_content, example_images = self._process_text_and_media(example_text, example_media_paths, is_example=True)

        return example_content, example_images

    def prepare_query_content(self, query_info):
        query_text = query_info.get("query_text", "")
        image_paths = query_info.get("image_paths", [])
        
        query_content, query_images = self._process_text_and_media(query_text, image_paths)

        return query_content, query_images

    def _set_patch_strategy(self, images, use_one=False):
        if len(images) > 8 or use_one:
            self.llm.llm_engine.model_config.hf_config.use_thumbnail = False
            self.llm.llm_engine.model_config.hf_config.max_dynamic_patch = 1
        elif len(images) > 4:
            self.llm.llm_engine.model_config.hf_config.use_thumbnail = True
            self.llm.llm_engine.model_config.hf_config.max_dynamic_patch = 2
        elif len(images) > 2:
            self.llm.llm_engine.model_config.hf_config.use_thumbnail = True
            self.llm.llm_engine.model_config.hf_config.max_dynamic_patch = 4
        else:
            self.llm.llm_engine.model_config.hf_config.use_thumbnail = True
            self.llm.llm_engine.model_config.hf_config.max_dynamic_patch = 6

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
            generated_text = None
            exceed_image_quota = self._set_sampling_config(query_idx)
            if not exceed_image_quota:
                images = []
                query_content, query_images = self.prepare_query_content(query_info)
                if context_image_list:
                    images.extend(context_image_list)
                if query_images:
                    images.extend(query_images)

                query_payload_list = context + query_content

                # Do not update the image patching strategy if in single-image setting
                # (all tasks will use only one image)
                self._set_patch_strategy(images)
                query_payload = "\n".join(query_payload_list)
                message = [{"role": "user", "content": query_payload}]

                prompt = self.tokenizer.apply_chat_template(
                    message, tokenize=False, add_generation_prompt=True
                )
                stop_tokens = ["<|endoftext|>", "<|im_start|>", "<|im_end|>", "<|end|>"]
                stop_token_ids = [
                    self.tokenizer.convert_tokens_to_ids(i) for i in stop_tokens
                ]
                max_new_tokens = self.config.get("session_len", 8192)
                sampling_params = SamplingParams(
                    temperature=0.0,
                    max_tokens=max_new_tokens,
                    stop_token_ids=stop_token_ids,
                )

                try:
                    outputs = self.llm.generate(
                        {
                            "prompt": prompt,
                            "multi_modal_data": {"image": images},
                        },
                        sampling_params=sampling_params,
                    )
                except (ValueError, RuntimeError):
                    # the prompt is too long, or the image patching leads to different image size, 
                    # Then force to reset the processor, fall back to use one image
                    self._set_patch_strategy(images, use_one=True)
                    try:
                        outputs = self.llm.generate(
                            {
                                "prompt": prompt,
                                "multi_modal_data": {"image": images},
                            },
                            sampling_params=sampling_params,
                        )
                    except Exception as e:
                        # if still fail, output the error info
                        outputs = str(e)

                if isinstance(outputs, list):
                    for o in outputs:
                        generated_text = o.outputs[0].text
                else:
                    generated_text = outputs

            else:
                generated_text = (
                    "Exceed the specified max number of images, skip running the model."
                )

            if self.print_response:
                print(f"Model response:\n {generated_text}")

            query_response.append(
                {
                    "response": generated_text,
                    "correct_answer": query_info["correct_answer"],
                }
            )

        return query_response

    def _process_text_and_media(self, text, media_paths, is_example=False):
        content = []
        images = []
        chunks = re.split(r'(<image>|<video>)', text)
        
        placeholder_count = sum(1 for chunk in chunks if chunk in ['<image>', '<video>'])
        
        if placeholder_count != len(media_paths):
            raise ValueError(f"Mismatch between number of placeholders ({placeholder_count}) and media paths ({len(media_paths)})")
        
        media_index = 0
        curr_demo_images = 0
        for chunk in chunks:
            if chunk == '<image>':
                if is_example and curr_demo_images >= self.max_demo_num_image:
                    logging.warning("Exceed the quota for demo image, skip the demo image")
                else:
                    image_content = self.create_media_content(media_paths[media_index], is_demo=is_example)
                    content.append("<image>")
                    images.extend(image_content)
                    if is_example:
                        curr_demo_images += 1
                media_index += 1
            elif chunk == '<video>':
                video_content = self.create_media_content(media_paths[media_index], is_demo=is_example)
                content.append(self.prompts["video_start"])
                for _ in video_content:
                    content.append("<image>")
                content.append(self.prompts["video_end"])
                images.extend(video_content)
                media_index += 1
            elif chunk.strip():  # Only add non-empty text chunks
                content.append(chunk.strip())
        
        return content, images
