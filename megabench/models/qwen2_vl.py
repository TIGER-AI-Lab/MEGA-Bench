import logging
from PIL import ImageFile
from tqdm import tqdm
from transformers import AutoProcessor
from qwen_vl_utils import process_vision_info
import pathlib
import json
from models.openai import OpenAI
from vllm import LLM, SamplingParams

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
ImageFile.LOAD_TRUNCATED_IMAGES = True


class Qwen2VL(OpenAI):
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
            max_num_seqs=5,
            max_model_len=32768,
            limit_mm_per_prompt={"image": max_num_image},
            tensor_parallel_size=kwargs.get("ngpus", 1),
            gpu_memory_utilization=kwargs.get("gpu_utils", 0.9),
        )

    @staticmethod
    def load_config(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def create_image_content(self, image_path):
        base64_image, mime_type = self.encode_image(image_path)
        # image format is modified
        return {
            "type": "image",
            "image": f"data:{mime_type};base64,{base64_image}",
        }

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
                query_payload = [{"role": "user", "content": context + query_content}]
                text = self.processor.apply_chat_template(
                    query_payload, tokenize=False, add_generation_prompt=True
                )
                image_inputs, _ = process_vision_info(query_payload)
                max_new_tokens = self.config.get("session_len", 8192)

                sampling_params = SamplingParams(
                    temperature=0.0, max_tokens=max_new_tokens, stop_token_ids=None
                )

                outputs = self.llm.generate(
                    {
                        "prompt": text,
                        "multi_modal_data": {"image": image_inputs},
                    },
                    sampling_params=sampling_params,
                )

                for o in outputs:
                    generated_text = o.outputs[0].text
                    print(generated_text)

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
