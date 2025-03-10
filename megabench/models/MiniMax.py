import logging
from PIL import ImageFile
import requests
from tqdm import tqdm
import pathlib
import json
from models.OpenAI import OpenAI
from openai import OpenAI as OpenAI_CLIENT
from vllm import LLM, SamplingParams

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
ImageFile.LOAD_TRUNCATED_IMAGES = True


class MiniMax(OpenAI):
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
        tp=None,
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
        
    def query(self, task_name, query_data, position=0):
        self.query_data = query_data
        self._set_sampling_config(0)
        context = self.prepare_context()
        client = OpenAI_CLIENT(
            api_key=self.api_key,  # <--your api key
            base_url="https://api.minimaxi.chat/v1",
        )

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
            message_content = ""

            if not exceed_image_quota:
                messages = self.prepare_system_message()
                messages.append(
                    {
                        "role": "user",
                        "name": "user",
                        "content": context + query_content,
                    }
                )
                response_data = None
                while response_data is None:
                    response = client.chat.completions.create(
                        model="MiniMax-Text-01",
                        messages=messages,
                        temperature=0.0,
                    )
                    try:
                        response_ = response.json()
                        if isinstance(response_, str):  # 如果是字符串
                            response_ = json.loads(response_)
                    except requests.exceptions.JSONDecodeError as e:
                        logging.info(f"Can't parse output: {e}, retry...")
                    if "error" in response_:
                        error_info = response_["error"]
                        logging.info(
                            f"Got error with type: {error_info['type']}. Message: {error_info['message']}"
                        )
                        logging.info(f"Retry...")
                    else:
                        response_data = response_
                        break

                print("response_data:", response_data)
                total_tokens = response_data.get("usage", {}).get("total_tokens", "N/A")
                    
                # Extracting the 'content' field from the response
                if response_data and "choices" in response_data:
                    choices = response_data["choices"]
                    if choices and "message" in choices[0]:
                        message_content = choices[0]["message"]["content"]
                        if self.print_response:
                            logging.info(
                                f"response: {message_content}; tokens:{total_tokens}"
                            )
                else:
                    message_content = ""
            else:
                message_content = (
                    "Exceed the specified max number of images, skip..."
                )

            if self.print_response:
                logging.info(f"Response: {message_content}")

            query_response.append(
                {
                    "response": message_content,
                    "correct_answer": query_info["correct_answer"],
                }
            )

        return query_response
