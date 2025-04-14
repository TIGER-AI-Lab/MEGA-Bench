import logging
from PIL import ImageFile, Image
from tqdm import tqdm
from transformers import AutoProcessor
import pathlib
import json
from models.openai import OpenAI
from vllm import LLM, SamplingParams
import re
from io import BytesIO
import base64
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
ImageFile.LOAD_TRUNCATED_IMAGES = True

class Llama4(OpenAI):
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
        self.processor = AutoProcessor.from_pretrained(model)
        self.llm = LLM(
            model=model,
            max_num_seqs=4,
            max_model_len=32768,
            limit_mm_per_prompt={"image": max_num_image},
            tensor_parallel_size=kwargs.get("ngpus", 1),
            gpu_memory_utilization=kwargs.get("gpu_utils", 0.9),
        )   
        # export VLLM_WORKER_MULTIPROC_METHOD=spawn 
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
        
    def query(self, task_name, query_data, position=0):
        self.query_data = query_data
        self._set_sampling_config(0)
        context, context_images = self.prepare_context()

        query_response = []
        generated_text = ""

        for query_idx, query_info in enumerate(
            tqdm(
                query_data["queries"],
                desc=f"{task_name} - Processing queries",
                unit="query",
                position=position,
            )
        ):
            exceed_image_quota = self._set_sampling_config(query_idx)
            query_content, query_images = self.prepare_query_content(query_info)
            if not exceed_image_quota:
                messages = []
                content = []
                images = []
                content.extend(context)
                content.extend(query_content)
                messages.append({"role": "user", "content": content})
                if context_images:
                    images.extend(context_images)
                if query_images:
                    images.extend(query_images)
                prompt = self.processor.apply_chat_template(
                    messages,
                    tokenize=False,
                    add_generation_prompt=True
                )
                sampling_params = SamplingParams(temperature=0.0,
                                     max_tokens=4096)

                outputs = self.llm.generate(
                    {
                        "prompt": prompt,
                        "multi_modal_data": {
                            "image": images
                        },
                    },
                    sampling_params=sampling_params
                    )

                for o in outputs:
                    generated_text = o.outputs[0].text
                    
                if generated_text.endswith("<|eot|>"):
                    generated_text = generated_text[:-7]  # 删除末尾的<|eot|>

            else:
                generated_text = (
                    "Exceed the specified max number of images, skip running the model."
                )

            if self.print_response:
                logging.info(f"Response: {generated_text}")

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
                    content.append({"type": "image","image": image_content,})
                    images.extend(image_content)
                    if is_example:
                        curr_demo_images += 1
                media_index += 1
            elif chunk == '<video>':
                video_content = self.create_media_content(media_paths[media_index], is_demo=is_example)
                content.append({"type": "text", "text": self.prompts["video_start"]})
                for image_url in video_content:
                    content.append({"type": "image","image": image_url,})
                content.append({"type": "text", "text": self.prompts["video_end"]}  )
                images.extend(video_content)
                media_index += 1
            elif chunk.strip():  # Only add non-empty text chunks
                content.append({"type": "text", "text": chunk.strip()})
        
        return content, images