import copy
import json
from typing import Any, Dict
import logging
import pathlib
from metrics import MetricType, AggregationType, ResponseParseType
from metrics.parsing.common.utils import evaluate_as_string
import os
import ast


class EvaluationProcessor:
    def __init__(
        self,
        hf_data,
        data_file: str,
        logging_file: str,
        output_score_file: str,
        sanity_check_eval: bool = False,
    ):
        self.data_file = data_file
        self.data = self._load_json(data_file)
        self.output_file = output_score_file
        self.eval_results = (
            self._load_json(output_score_file)
            if pathlib.Path(output_score_file).exists()
            else {"data": self.data}
        )
        self.sanity_check_eval = sanity_check_eval

        # Configure logging
        self.file_logger = logging.getLogger("errorLogger")
        file_handler = logging.FileHandler(logging_file, "w+")
        file_handler.setLevel(logging.ERROR)
        self.file_logger.addHandler(file_handler)
        self.file_logger.propagate = False  # Prevent propagation to the root logger

        self.console_logger = logging.getLogger("infoLogger")
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        self.console_logger.addHandler(console_handler)
        self.console_logger.propagate = False  # Prevent propagation to the root logger

        self.scoring_functions = {}
        for task in hf_data:
            self.scoring_functions[task["task_name"]] = ast.literal_eval(
                task["task_samples"][0]["metric_info"]
            )

        self.organized_hf_data = {}
        for task in hf_data:
            self.organized_hf_data[task["task_name"]] = task["task_samples"]

    def _get_eval_context(self, task_name, query):
        query_index = query["task_idx"]
        eval_context = self.organized_hf_data[task_name][query_index]["eval_context"]
        eval_context = ast.literal_eval(eval_context)
        return eval_context

    def _load_json(self, file_path: str) -> Any:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _sync_scores(self) -> None:
        """
        Sync existing scores to self.data
        """
        if not self.eval_results:
            return

        existing_task_map = {
            task["task_name"]: task for task in self.eval_results["data"]
        }

        for task in self.data:
            task_name = task.get("task_name", "")
            if task_name in existing_task_map:
                existing_task = existing_task_map[task_name]
                if len(task["query_response"]) == len(existing_task["query_response"]):
                    # Sync the scores
                    task["task_score"] = existing_task.get("task_score", -1)
                    task["mean_task_score"] = existing_task.get("mean_task_score", -1)
                    for query_idx, query in enumerate(task["query_response"]):
                        existing_query = existing_task["query_response"][query_idx]
                        query["scores"] = existing_query.get("scores", {})

    def _determine_eval_style(self, task):
        metric_info = self.scoring_functions[task["task_name"]]
        all_task_metrics = list(metric_info["field_score_function"].values())
        eval_type = (
            "rule"
            if (
                "gpt_4o_as_judge" not in all_task_metrics
                and "ascii_art_gpt4o_judge" not in all_task_metrics
            )
            else "llm"
        )
        return eval_type

    def _check_task_needs_evaluate(self, task: Dict, eval_type: str) -> bool:
        if not self.eval_results:
            return True

        task_exist = False
        for existing_task in self.eval_results["data"]:
            if task.get("task_name") == existing_task.get("task_name"):
                # rule-eval tasks are fast and easy to run, we can always re-evaluate them
                if eval_type == "rule":
                    return True

                # Do not re-evaluate gpt-4o-as-judge, unless it's nenessary
                task_exist = existing_task
                if len(task["query_response"]) != len(existing_task["query_response"]):
                    return True
                for res_example, saved_example in zip(
                    task["query_response"], existing_task["query_response"]
                ):
                    if (
                        res_example["response"] != saved_example["response"]
                        or res_example["correct_answer"]
                        != saved_example["correct_answer"]
                    ):
                        # model output or gt answer changed
                        return True
                    elif (
                        "scores" not in saved_example
                        or "query" not in saved_example["scores"]
                    ):
                        # no existing eval results (not evaluated before)
                        return True
                    elif (
                        saved_example["scores"]["query"] == -1
                        and len(saved_example["scores"]["field"]) == 0
                    ):
                        return True
                    elif (
                        "eval_context" not in saved_example
                        and "eval_context" in res_example
                    ) or (res_example["eval_context"] != saved_example["eval_context"]):
                        # the eval context changed
                        return True
                    else:
                        # nothing changed, using the old eval results
                        res_example["scores"] = saved_example["scores"]

                task["mean_task_score"] = existing_task["mean_task_score"]
                task["task_score"] = existing_task["task_score"]

        if not task_exist:
            return True

        return False

    def _determine_skip_eval(self, task, eval_type):
        # Skip the task if it has already been evaluated
        evaluated = False
        if not self._check_task_needs_evaluate(task, eval_type):
            self.console_logger.info(
                f"{task['task_name']} already evaluated, skipping..."
            )
            skip_eval = True
            evaluated = True
        else:
            skip_eval = False
        return skip_eval, evaluated

    @staticmethod
    def load_task_metrics(task_info, score_function_table):
        fields = list(task_info["query_response"][0]["correct_answer"].keys())
        answer_fields = [item for item in fields if not item.startswith("##")]
        metrics = {}
        for field in fields:
            scoring_function_name = score_function_table["field_score_function"].get(
                field
            )
            metric = MetricType.from_string(scoring_function_name)
            if metric == MetricType.GPT_4O_AS_JUDGE:
                gpt4o_metric_config = score_function_table["gpt4o_eval_configs"]
                metric = metric.class_impl(gpt4o_metric_config)
            metrics[field] = metric
        global_aux_fields = score_function_table.get("global_aux_metrics", {})
        for field, scoring_function_name in global_aux_fields.items():
            metric = MetricType.from_string(scoring_function_name)
            if metric == MetricType.GPT_4O_AS_JUDGE:
                gpt4o_metric_config = score_function_table["gpt4o_eval_configs"]
                metric = metric.class_impl(gpt4o_metric_config)
            metrics[field] = metric

        return metrics, answer_fields

    def process(self, single_task_name=None) -> None:
        # if eval all tasks, sync the scores
        if not single_task_name:
            self._sync_scores()

        num_tasks_evaluated = {"rule": 0, "llm": 0}
        num_queries_evaluated = {"rule": 0, "llm": 0}
        num_tasks_unevaluated = {"rule": 0, "llm": 0}
        num_queries_unevaluated = {"rule": 0, "llm": 0}
        num_samples_all = {"rule": 0, "llm": 0}
        per_query_model_score = {"rule": 0, "llm": 0}
        per_task_model_score = {"rule": 0, "llm": 0}

        # For the ground truth sanity check
        imperfect_score_tasks = set()

        for task in self.data:
            task_name = task.get("task_name", "")
            task_folder = task.get("directory", "")
            task_info = {
                "task_name": task_name,
                "task_folder": task_folder,
                "results_file": self.data_file,
            }
            # Only evaluate a single task for fast check
            if single_task_name and task_name != single_task_name:
                continue

            eval_type = self._determine_eval_style(task)
            skip_eval, evaluated = self._determine_skip_eval(task, eval_type)
            task["eval_type"] = eval_type  # add the eval_type info into the task data

            if skip_eval:
                num_samples_all[eval_type] += len(task["example_contents"]) + len(
                    task["query_response"]
                )
                if evaluated:  # skipped and already evaluated, update the stats
                    num_tasks_evaluated[eval_type] += 1
                    num_queries_evaluated[eval_type] += len(task["query_response"])
                    per_task_model_score[eval_type] += task["mean_task_score"]
                    per_query_model_score[eval_type] += task["task_score"]
                    self.console_logger.info(
                        f"task: {task_name}, score: {task['task_score']} / {len(task['query_response'])}"
                    )
                else:
                    num_tasks_unevaluated[eval_type] += 1
                    num_queries_unevaluated[eval_type] += len(task["query_response"])
                    self.console_logger.info(
                        f"task: {task_name} skipped and not evaluated yet!"
                    )

                continue

            self.console_logger.info(f"Start evaluating {task['task_name']}...")

            if "query_response" in task:
                scoring_function_table = self.scoring_functions.get(
                    task_name,
                    {
                        "field_score_function": {},
                        "aggregation": {"function": None, "field_weights": {}},
                        "response_parse_function": None,
                    },
                )

                num_tasks_evaluated[eval_type] += 1
                num_demo = 1 if len(task["example_info"]) > 0 else 0
                num_samples_all[eval_type] += len(task["query_response"]) + num_demo
                task_score = 0

                field_score_function_table: dict = scoring_function_table[
                    "field_score_function"
                ]
                task_metrics, answer_fields = self.load_task_metrics(
                    task, scoring_function_table
                )
                global_aux_metrics = scoring_function_table.get(
                    "global_aux_metrics", {}
                )
                res_parser_type = scoring_function_table["response_parse_function"]
                parser = ResponseParseType.from_string(res_parser_type)

                for query_idx, query in enumerate(task["query_response"]):
                    response = query["response"]
                    correct_answer = query["correct_answer"]
                    num_queries_evaluated[eval_type] += 1

                    res_parsing_pass = True
                    if parser.is_single_field_parser():
                        # single field
                        assert (
                            len(answer_fields) == 1
                        ), "The answer_string parse must be used when the answer has a single field"
                        answer_key = answer_fields[0]

                        global_description = task["global_description"]
                        query_question = query["query_text"]
                        is_single_line_ans = "\n" not in correct_answer[answer_key]

                        response_obj = parser.parse(
                            response,
                            answer_key,
                            global_description=global_description,
                            query_question=query_question,
                            is_single_line_ans=is_single_line_ans,
                        )
                        if isinstance(
                            correct_answer[answer_key], dict
                        ) and not isinstance(response_obj[answer_key], dict):
                            res_parsing_pass = False
                    else:
                        # Structural output (using JSON parser or other specified parsing func) or dummy parse (return all)
                        response_obj = parser.parse(response)

                        if parser == ResponseParseType.JSON and (
                            not isinstance(response_obj, dict) or not response_obj
                        ):
                            # Expect a JSON, but parsing failed,
                            # Record the failure parsing, and use the raw string for each field of the answer
                            res_parsing_pass = False
                            response_obj = {}
                            for field in correct_answer:
                                response_obj[field] = response

                    if not res_parsing_pass:
                        # logging the parsing failure
                        self.console_logger.info(
                            f"Response parsing failed for {task_name}, query index: {query_idx+1}, use the raw output instead"
                        )
                        self.file_logger.error(
                            f"Task:{task_name}, cannot parse {response}"
                        )

                    query["scores"] = {"field": {}, "info": {}}

                    for field, correct_value in correct_answer.items():
                        self.evaluate_field(
                            task_name=task_name,
                            task_info=task_info,
                            field_score_function_table=field_score_function_table,
                            task_metrics=task_metrics,
                            query_idx=query_idx,
                            query=query,
                            correct_answer=correct_answer,
                            response_obj=response_obj,
                            field=field,
                            correct_value=correct_value,
                        )

                    # Add global auxiliary metrics
                    original_response_obj = copy.deepcopy(response_obj)
                    for field in global_aux_metrics:
                        response_obj[field] = original_response_obj
                        self.evaluate_field(
                            task_name=task_name,
                            task_info=task_info,
                            field_score_function_table=field_score_function_table,
                            task_metrics=task_metrics,
                            query_idx=query_idx,
                            query=query,
                            correct_answer=correct_answer,
                            response_obj=response_obj,
                            field=field,
                            correct_value=correct_answer,
                        )

                    aggregator = AggregationType.from_string(
                        scoring_function_table["aggregation"]["function"]
                    )
                    query["scores"]["query"] = aggregator.aggregate(
                        query["scores"]["field"],
                        scoring_function_table["aggregation"]["field_weights"],
                    )

                    if query["scores"]["query"] >= 0:
                        task_score += query["scores"]["query"]

                if task_score < 0:
                    task["task_score"] = -1
                    task["mean_task_score"] = -1
                else:
                    task["task_score"] = task_score
                    if task["query_response"]:
                        task["mean_task_score"] = task_score / len(
                            task["query_response"]
                        )
                    else:
                        task["mean_task_score"] = 0
                    per_task_model_score[eval_type] += task["mean_task_score"]
                    per_query_model_score[eval_type] += task_score

                self.console_logger.info(
                    f"task: {task_name}, score: {task_score} / {len(task['query_response'])}"
                )
                if self.sanity_check_eval and task["mean_task_score"] != 1:
                    imperfect_score_tasks.add((task_name, task["mean_task_score"]))

                if not single_task_name:
                    self._save_json_safe(
                        self.output_file,
                        {
                            "data": self.data,
                            "temp_summary": {
                                "num_tasks_evaluated": num_tasks_evaluated,
                                "num_queries_evaluated": num_queries_evaluated,
                                "num_samples_all": num_samples_all,
                            },
                        },
                    )

        if self.sanity_check_eval:
            self.file_logger.error(
                "\n\n### Sanity Check Eval: Imperfect Score Tasks ###"
            )
            for task_name, task_score in imperfect_score_tasks:
                self.file_logger.error(
                    f"    Failed task: {task_name}, score: {task_score}"
                )

        macro_mean_score = {}
        micro_mean_score = {}
        for eval_type in num_tasks_evaluated:
            macro_mean_score[eval_type] = (
                float(per_task_model_score[eval_type] / num_tasks_evaluated[eval_type])
                if num_tasks_evaluated[eval_type] > 0
                else 0
            )
            micro_mean_score[eval_type] = (
                float(
                    per_query_model_score[eval_type] / num_queries_evaluated[eval_type]
                )
                if num_queries_evaluated[eval_type] > 0
                else 0
            )

        macro_mean_score_overall = sum(per_task_model_score.values()) / sum(
            num_tasks_evaluated.values()
        )
        micro_mean_score_overall = sum(per_query_model_score.values()) / sum(
            num_queries_evaluated.values()
        )

        summary = {
            "num_tasks_evaluated": num_tasks_evaluated,
            "num_tasks_unevaluated": num_tasks_unevaluated,
            "num_queries_evaluated": num_queries_evaluated,
            "num_queries_unevaluated": num_queries_unevaluated,
            "num_samples_all": num_samples_all,
            "macro_mean_score": macro_mean_score,
            "micro_mean_score": micro_mean_score,
            "overall_macro_mean_score": macro_mean_score_overall,
            "overall_micro_mean_score": micro_mean_score_overall,
        }

        if not single_task_name:
            self._save_json_safe(
                self.output_file,
                {"data": self.data, "summary": summary},
            )

        self.console_logger.info(
            f"Evaluation results: \n{json.dumps(summary, indent=4)}"
        )
        self.console_logger.info(
            f"Evaluation Complete! Result saved in {self.output_file}"
        )

    def evaluate_field(
        self,
        task_name,
        task_info,
        field_score_function_table,
        task_metrics,
        query_idx,
        query,
        correct_answer,
        response_obj,
        field,
        correct_value,
    ):
        metric = task_metrics[field]
        eval_context = self._get_eval_context(task_name, query)

        # drop duplicate string notation
        correct_value = evaluate_as_string(correct_value)

        if self.sanity_check_eval:
            if metric == MetricType.PROGRAM_JUDGE:
                # Some programming tasks are evaluated with test cases,
                # there is no ground truth code provided
                # The answer of the 1-shot demonstration examples are all tested
                should_skip = True
            else:
                should_skip = correct_value == ""
        else:
            should_skip = False

        if should_skip:
            query["scores"]["field"][field] = 1
            if metric in [
                MetricType.CONSTRAINED_GENERATION,
                MetricType.XML_NORM_POINT_IN_BBOX,
                MetricType.GPT_4O_AS_JUDGE,
            ]:
                query["scores"]["info"][
                    field
                ] = "Metric skipped because no ground truth was provided for the task."
            return

        if metric == MetricType.UNSUPPORTED:
            self.console_logger.warning(
                f"The metric for {field} in task {task_name} is not supported"
            )
            self.file_logger.error(
                f'The metric for {field} in task {task_name}: "{field_score_function_table[field]}" is not supported'
            )
        elif metric == MetricType.SYMBOLIC_PLANNING_TEST:
            query["scores"]["field"][field] = metric.match(
                response_obj.get(field),
                eval_context,
                task_info,
            )
        elif metric == MetricType.PROGRAM_JUDGE:
            query["scores"]["field"][field] = metric.match(
                response_obj.get(field), eval_context, task_info
            )
        elif metric == MetricType.CONSTRAINED_GENERATION:
            score, eval_info = metric.match(response_obj, eval_context)
            query["scores"]["field"][field] = score
            query["scores"]["info"][field] = eval_info
        elif metric == MetricType.XML_NORM_POINT_IN_BBOX:
            score, eval_info = metric.match(response_obj.get(field), eval_context)
            query["scores"]["field"][field] = score
            query["scores"]["info"][field] = eval_info
        elif metric == MetricType.GPT_4O_AS_JUDGE:
            response_info = (
                response_obj.get(field)
                if isinstance(response_obj, dict)
                else response_obj
            )
            score, eval_info = metric.match(
                response_info,
                correct_answer,
                query["images"],
                query["query_text"],
                eval_context,
            )
            query["scores"]["field"][field] = score
            query["scores"]["info"][field] = eval_info
        else:
            query["scores"]["field"][field] = metric.match(
                response_obj.get(field), correct_value
            )

        if self.sanity_check_eval and query["scores"]["field"][field] != 1:
            if (
                metric == MetricType.POSITIVE_INT_MATCH
                and int(correct_value) <= 0
                and int(response_obj.get(field)) <= 0
            ):
                return
            score = query["scores"]["field"][field]
            self.file_logger.error(
                f"Example did not get a score of 1: {task_name=}, {field=}, {query['task_idx']=}, {score=}"
            )

    def _save_json_safe(self, file_path: str, data: Any) -> None:
        temp_filename = str(file_path) + ".tmp"
        with open(temp_filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        os.replace(temp_filename, file_path)
