import logging
from PIL import Image, ImageFile
from mimetypes import guess_type
from tqdm import tqdm
import pathlib
import torch
import json
import warnings
import re
from models.openai import OpenAI
from transformers import AutoModelForCausalLM
from deepseek_vl2.models import DeepseekVLV2Processor, DeepseekVLV2ForCausalLM
from deepseek_vl2.utils.io import load_pil_images
import tempfile
import os

warnings.filterwarnings("ignore")
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
ImageFile.LOAD_TRUNCATED_IMAGES = True

logger = logging.getLogger("infoLogger")


class DeepSeekVL2(OpenAI):
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

        self.vl_chat_processor: DeepseekVLV2Processor = DeepseekVLV2Processor.from_pretrained(model)
        self.tokenizer = self.vl_chat_processor.tokenizer
        
        vl_gpt: DeepseekVLV2ForCausalLM = AutoModelForCausalLM.from_pretrained(model, trust_remote_code=True)
        self.model = vl_gpt.to(torch.bfloat16).cuda().eval()
    
    @staticmethod
    def split_model(model_name):
        device_map = {}
        model_splits = {
            'deepseek-ai/deepseek-vl2-small': [13, 14], # 2 GPU for 16b
            'deepseek-ai/deepseek-vl2': [10, 10, 10], # 3 GPU for 27b
        }
        if model_name not in model_splits:
            return None
        num_layers_per_gpu = model_splits[model_name]
        num_layers =  sum(num_layers_per_gpu)
        layer_cnt = 0
        for i, num_layer in enumerate(num_layers_per_gpu):
            for j in range(num_layer):
                device_map[f'language.model.layers.{layer_cnt}'] = i
                layer_cnt += 1
        device_map['vision'] = 0
        device_map['projector'] = 0
        device_map['image_newline'] = 0
        device_map['view_seperator'] = 0
        device_map['language.model.embed_tokens'] = 0
        device_map['language.model.norm'] = 0
        device_map['language.lm_head'] = 0
        device_map[f'language.model.layers.{num_layers - 1}'] = 0
        return device_map

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
                    content.append("<image>")
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
                    content.append("<image>")
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
    
    def _create_temp_image_list(self, images):
        tmp_dir = tempfile.mkdtemp()
        
        tmp_paths = []
        # First process all images
        for i, img in enumerate(images):
            tmp_path = os.path.join(tmp_dir, f"img_{i}.png")
            img.save(tmp_path)
            tmp_paths.append(tmp_path)
        
        return tmp_paths

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

                query_payload_list = context + query_content
                query_payload = "\n".join(query_payload_list)
                image_list = self._create_temp_image_list(images)

                conversation = [
                    {
                        "role": "<|User|>",
                        "content": query_payload,
                        "images": image_list,
                    },
                    {"role": "<|Assistant|>", "content": ""}
                ]

                pil_images = load_pil_images(conversation)
                prepare_inputs = self.vl_chat_processor(
                    conversations=conversation,
                    images=pil_images,
                    force_batchify=True,
                    system_prompt=""
                ).to(self.model.device)

                # run image encoder to get the image embeddings
                inputs_embeds = self.model.prepare_inputs_embeds(**prepare_inputs)

                try:
                    outputs = self.model.language.generate(
                        inputs_embeds=inputs_embeds,
                        attention_mask=prepare_inputs.attention_mask,
                        pad_token_id=self.tokenizer.eos_token_id,
                        bos_token_id=self.tokenizer.bos_token_id,
                        eos_token_id=self.tokenizer.eos_token_id,
                        max_new_tokens=8192,
                        do_sample=False,
                        use_cache=True,
                    )
                    text_outputs = self.tokenizer.decode(outputs[0].cpu().tolist(), skip_special_tokens=True)
                except TimeoutError as e:
                    text_outputs = str(e)
            else:
                text_outputs = (
                    "Exceed the specified max number of images, skip running the model."
                )

            if self.print_response:
                print("Model response:", text_outputs)

            query_response.append(
                {
                    "response": text_outputs,
                    "correct_answer": query_info["correct_answer"],
                }
            )
        return query_response
