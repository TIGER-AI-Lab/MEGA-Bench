import logging
from metrics.metric_type import MetricType
from metrics.scoring.common.conversions import str_to_list
from models.base_model import BaseModel
from tqdm import tqdm
from metrics.scoring.multi_ref_phrase import replace_potential_chinese_comma


class GroundTruthOracle(BaseModel):

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
        """Return the ground truth."""
        self.query_data = query_data

        query_response = []
        metrics = self.query_data["metric_info"]["field_score_function"]

        for query_idx, query_info in enumerate(
            tqdm(
                query_data["queries"],
                desc=f"{task_name} - Processing queries",
                unit="query",
                position=position,
                mininterval=0.1,
                miniters=1,
            )
        ):
            response = correct_answer = query_info["correct_answer"]
            assert isinstance(correct_answer, dict)

            # Process the response to match what we produce for the other models.
            for field_name in response:
                if metrics[field_name] == MetricType.MULTI_REF_PHRASE_EVAL.value:
                    # We take the first option for multi-ref phrase evaluation.
                    try:
                        field_res = replace_potential_chinese_comma(
                            response[field_name]
                        )
                        response[field_name] = str(str_to_list(field_res)[0])
                    except IndexError as e:
                        raise IndexError(
                            f"Example for {task_name=}, {field_name=}, index {i=} has an invalid multi_ref ground truth!"
                        ) from e
            if len(response) == 1:
                response = list(response.values())[0]

            response = str(response)
            response = f"I have access to the ground truth answer, so I'll just return that.\n\nAnswer:{response}"

            if self.print_response:
                logging.info(f"response {query_idx}: {response}")
            query_response.append(
                {"response": response, "correct_answer": correct_answer}
            )

        return query_response

    def create_image_content(self):
        pass

    def prepare_context(self):
        pass

    def prepare_example_content(self):
        pass

    def prepare_query_content(self):
        pass
