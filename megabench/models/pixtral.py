from models.claude import Claude
import logging
import torch
from tqdm import tqdm
from vllm import LLM
from vllm.sampling_params import SamplingParams
import math


MAX_OUTPUT_TOKENS = 8192
MAX_TOKENS_PER_IMAGE = 4096
SAMPLING_PARAMS = SamplingParams(temperature=0, max_tokens=MAX_OUTPUT_TOKENS)


class Pixtral(Claude):

    def __init__(
        self,
        api_key=None,
        model=None,
        query_data=None,
        resize=True,
        max_side=1000,
        print_response=False,
        max_num_image=None,
        system_message: str | None = None,
        total_demo_video_frames=4,
        **kwargs,
    ):
        super().__init__(
            api_key=api_key,
            model=model,
            query_data=query_data,
            resize=resize,
            max_side=max_side,
            print_response=print_response,
            max_num_image=max_num_image,
            system_message=system_message,
            total_demo_video_frames=total_demo_video_frames,
            **kwargs,
        )
        self.kwargs = kwargs
        self.llm = LLM(**self.make_model_kwargs())
        self.ATTEMPT_LIMIT = 5

    def make_model_kwargs(self):
        """Set the LLM loading configuration."""
        kwargs = dict(
            model=self.model,
            max_num_seqs=5,
            trust_remote_code=True,
            limit_mm_per_prompt={"image": self.max_num_image},
            tensor_parallel_size=self.kwargs.get("ngpus", 1),
            gpu_memory_utilization=self.kwargs.get("gpu_utils", 0.9),
            tokenizer_mode="mistral",
            max_num_batched_tokens=self.max_num_image * MAX_TOKENS_PER_IMAGE,
        )

        num_gpus = torch.cuda.device_count()
        if num_gpus:
            kwargs["tensor_parallel_size"] = num_gpus

        return kwargs

    def create_image_content(self, image_path):
        base64_image, mime_type = self.encode_image(image_path)
        return {
            "type": "image_url",
            "image_url": {"url": f"data:{mime_type};base64,{base64_image}"},
        }

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
                text_content = None
                n_attempt = 0
                context_ = context  # avoid changing the context for later queries
                while text_content is None:
                    messages = self.prepare_system_message()
                    try:
                        messages.append(
                            {"role": "user", "content": context_ + query_content}
                        )
                        response = self.llm.chat(
                            messages, sampling_params=SAMPLING_PARAMS
                        )[0]
                        text_content = response.outputs[0].text
                        metrics = response.metrics
                        is_finished = response.finished
                    except ValueError as e:
                        logging.warning(
                            f"Error: {e}. Retry {n_attempt}/{self.ATTEMPT_LIMIT}..."
                        )
                        n_attempt += 1
                        context_, query_content = self._prepare_data_with_lower_rate(
                            query_info, query_idx, 1 + n_attempt * 0.2
                        )
                        if n_attempt > self.ATTEMPT_LIMIT:
                            text_content = str(e)
                            metrics = ""
                            is_finished = False

            else:
                text_content = (
                    "Exceed the specified max number of images, skip running the model."
                )
                metrics = ""
                is_finished = False

            if self.print_response:
                logging.info(
                    f"Model response: {text_content}\n Metrics: {metrics}\n is_finished: {is_finished}"
                )
            query_response.append(
                {
                    "response": text_content,
                    "correct_answer": query_info["correct_answer"],
                }
            )

        return query_response
