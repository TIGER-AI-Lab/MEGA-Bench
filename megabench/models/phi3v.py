import logging
from tqdm import tqdm
import pathlib
import json
from models.internvl import InternVL
from models.openai import OpenAI
from transformers import AutoModelForCausalLM, AutoProcessor
import re


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Phi3v(InternVL):
    """
        Reuse all query preparation functions from InternVL, 
        only need to implement the prompt composition here
        But we don't call InternVL's init function, which avoids loading the model
    """
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
        super(OpenAI, self).__init__(
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

        self.model = AutoModelForCausalLM.from_pretrained(
            model,
            device_map="auto",
            trust_remote_code=True,
            torch_dtype="auto",
            _attn_implementation="flash_attention_2",
        )

        self.processor = AutoProcessor.from_pretrained(
            model, trust_remote_code=True, num_crops=4
        )

    @staticmethod
    def load_config(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def _preprocess_payload(self, payload):
        image_count = 0
        
        def replace_image_placeholder(_):
            nonlocal image_count
            image_count += 1
            return f"<|image_{image_count}|>"
        
        composed_prompt = re.sub(r'<image>', replace_image_placeholder, payload)
        messages = [{
            "role": "user",
            "content": composed_prompt
        },]
        return messages

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
                query_content, query_images = self.prepare_query_content(query_info)
                if context_image_list:
                    images.extend(context_image_list)
                if query_images:
                    images.extend(query_images)

                query_payload_list = context + query_content
                query_payload = "\n".join(query_payload_list)
                messages = self._preprocess_payload(query_payload)

                prompt = self.processor.tokenizer.apply_chat_template(
                    messages, tokenize=False, add_generation_prompt=True
                )
                inputs = self.processor(prompt, images, return_tensors="pt").to(
                    "cuda:0"
                )
                max_new_tokens = self.config.get("session_len", 8192)
                generation_args = {
                    "max_new_tokens": max_new_tokens,
                    "temperature": 0.0,
                    "do_sample": False,
                }

                import signal
                def handler(signum, frame):
                    raise TimeoutError("Function call timed out")

                timeout = self.config.get("timeout", 60)
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(timeout)

                try:
                    generate_ids = self.model.generate(
                        **inputs,
                        eos_token_id=self.processor.tokenizer.eos_token_id,
                        **generation_args,
                    )

                    # remove input tokens
                    generate_ids = generate_ids[:, inputs["input_ids"].shape[1] :]
                    response = self.processor.batch_decode(
                        generate_ids,
                        skip_special_tokens=True,
                        clean_up_tokenization_spaces=False,
                    )[0]

                except TimeoutError as e:
                    response = str(e)
                finally:
                    signal.alarm(0)

            else:
                response = (
                    "Exceed the specified max number of images, skip running the model."
                )

            if self.print_response:
                print(f"Model response:\n {response}")

            query_response.append(
                {
                    "response": response,
                    "correct_answer": query_info["correct_answer"],
                }
            )

        return query_response
