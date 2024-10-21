from functools import cached_property
import json
import pathlib
import logging
from multiprocessing import Pool, current_process, cpu_count
from filelock import FileLock, Timeout
from models.model_type import ModelType
import ast


class TaskProcessor:
    def __init__(
        self,
        output_file,
        model_type,
        print_response=False,
        model_path=None,
        force_regenerate=False,
        **kwargs,
    ):
        self.output_file = output_file
        self.model_type = ModelType.from_string(model_type)
        self.print_response = print_response
        self.model_path = model_path
        self.force_regenerate = force_regenerate
        self.model_kwargs = kwargs
        self.ensure_output_file_exists()

    @cached_property
    def output_path(self) -> pathlib.Path:
        return pathlib.Path(self.output_file)

    def read_all_query_responses(self):
        if self.output_path.exists():
            with self.output_path.open("r", encoding="utf-8") as file:
                return json.load(file)
        return []

    def write_all_query_responses(self, all_query_responses):
        with self.output_path.open("w", encoding="utf-8") as f:
            json.dump(all_query_responses, f, ensure_ascii=False, indent=4)

    def ensure_output_file_exists(self):
        if not self.output_path.exists():
            self.write_all_query_responses([])

    def append_query_response(self, response_data):
        lock_path = self.output_path.with_suffix(".lock")
        with FileLock(lock_path):
            all_query_responses = self.read_all_query_responses()
            if response_data not in all_query_responses:
                all_query_responses.append(response_data)
                self.write_all_query_responses(all_query_responses)

    def did_prompts_or_images_change(self, response, query_data):
        if len(response["query_response"]) != len(query_data["queries"]):
            logging.debug(
                f"The number of saved queries does not match the new query number, re-run the query..."
            )
            return True

        if response["global_description"] != query_data["global_description"]:
            logging.debug(
                f'Global description changed. {response["global_description"]=}, {query_data["global_description"]=}'
            )
            return True
        if response["global_images"] != query_data["global_images"]:
            logging.debug(
                f'Global images changed. {response["global_images"]=}, {query_data["global_images"]=}'
            )
            return True

        response_examples = [
            {"image_paths": ex["images"], "query_text": ex["query_text"]}
            for ex in response["query_response"]
        ]
        query_examples = [
            {k: v for k, v in ex.items() if k in ("image_paths", "query_text")}
            for ex in query_data["queries"]
        ]
        if str(response_examples) != str(query_examples):
            return True
        return False

    def _set_response_at_index(self, all_query_responses, response, i):
        all_query_responses = (
            all_query_responses[:i] + response + all_query_responses[i + 1 :]
        )
        self.write_all_query_responses(all_query_responses)

    def set_response_at_index(self, all_query_responses, response, i):
        self._set_response_at_index(all_query_responses, [response], i)

    def remove_response_at_index(self, all_query_responses, i):
        self._set_response_at_index(all_query_responses, [], i)

    def update_ground_truth_inplace(self, response, query_data) -> bool:
        needs_to_be_updated = False
        for resp_ex, query_ex in zip(response["query_response"], query_data["queries"]):
            correct_answer = query_ex["query_answer"]
            correct_answer_str = str(query_ex["query_answer"])
            resp_answer_str = str(resp_ex["correct_answer"])
            if resp_answer_str != correct_answer_str:
                logging.debug("Detect annotation change!")
                logging.debug("Latest answer from annotation:", correct_answer)
                logging.debug("Old answer from output file:", resp_ex["correct_answer"])
                needs_to_be_updated = True
                resp_ex["correct_answer"] = correct_answer
        return needs_to_be_updated

    def task_already_processed(self, task_name, query_data):
        output_path = pathlib.Path(self.output_file)
        if output_path.exists():
            lock_path = output_path.with_suffix(".lock")
            lock = FileLock(lock_path, timeout=5)
            try:
                with lock:
                    with open(output_path, "r", encoding="utf-8") as f:
                        all_query_responses = json.load(f)
            except Timeout:
                # Handle the timeout situation, e.g., retry or log an error
                print(f"Could not acquire the lock for {output_path}.")
            except json.JSONDecodeError as e:
                # Handle the JSON decode error
                print(f"Failed to decode JSON: {e}")

            for i, response in enumerate(all_query_responses):
                if response.get("task_name") == task_name:
                    if self.did_prompts_or_images_change(response, query_data):
                        logging.info("Prompt/image change detected")
                        # Remove old answer from all_query_responses
                        self.remove_response_at_index(all_query_responses, i)
                        return False
                    if self.force_regenerate:
                        logging.info("Regenerating answer...")
                        # Remove old answer from all_query_responses
                        self.remove_response_at_index(all_query_responses, i)
                        return False
                    did_ground_truth_change = self.update_ground_truth_inplace(
                        response, query_data
                    )
                    if did_ground_truth_change:
                        logging.warning(
                            f"Changes detected in {task_name}, update output file in place"
                        )
                        logging.debug(response)
                        self.set_response_at_index(all_query_responses, response, i)
                    return True
        return False

    def prepare_response_data(self, task_name, query_data, query_response):
        global_description = query_data["global_description"]
        global_images = query_data["global_images"]
        example_info = query_data["example_info"]
        queries = query_data["queries"]

        updated_query_response = self.update_query_response(query_response, queries)

        return {
            "task_name": task_name,
            "global_description": global_description,
            "global_images": global_images,
            "example_info": example_info,
            "query_response": updated_query_response,
        }

    def update_query_response(self, query_response, examples):
        for i, query in enumerate(query_response):
            query["global_idx"] = examples[i]["global_idx"]
            query["task_idx"] = examples[i]["task_idx"]
            query["images"] = examples[i]["image_paths"]
            query["query_text"] = examples[i]["query_text"]
        return query_response

    def check_processed_samples(self, tasks):
        skipped, to_be_processed = [], []
        for task in tasks:
            task_name = task["task_name"]
            query_data = self.construct_query_data(task)

            if self.task_already_processed(task_name, query_data):
                logging.info(f"Task {task_name} already processed. Skipping...")
                skipped.append(task)
            else:
                to_be_processed.append(task)
        return skipped, to_be_processed

    def process_task(self, task_item, model) -> bool:
        if model is None:
            model = self.model_type.get_model_instance(
                print_response=self.print_response,
                model_path=self.model_path,
                **self.model_kwargs,
            )

        task_name = task_item["task_name"]
        include_metrics = (
            True
            if self.model_type == ModelType.GROUND_TRUTH_ORACLE_SANITY_CHECK
            else False
        )
        query_data = self.construct_query_data(task_item, include_metrics)

        logging.info(f"Processing {task_name}...")

        process_id = (
            current_process()._identity[0] if current_process()._identity else 0
        )
        query_response = model.query(
            task_name=task_name, query_data=query_data, position=process_id
        )

        response_data = self.prepare_response_data(
            task_name, query_data, query_response
        )

        self.append_query_response(response_data)
        return True

    def process_all_tasks(
        self, single_task_name=None, processes=None, multiprocess=True, data=None
    ):
        num_new_tasks = 0
        tasks_to_process = []

        if single_task_name:
            logging.info(f"Processing single task: {single_task_name}")
            tasks_to_process = [
                item for item in data if item["task_name"] == single_task_name
            ]
            if not tasks_to_process:
                logging.error(f"Task '{single_task_name}' not found in dataset.")
        else:
            tasks_to_process = data

        # Load the model outside of the multiprocessing context if running locally
        # otherwise, load the model inside each task's process to facilitate MP
        if "KEY" in self.model_type.value[2]:
            model = None
        else:
            model = self.model_type.get_model_instance(
                print_response=self.print_response,
                model_path=self.model_path,
                **self.model_kwargs,
            )

        skipped_tasks, tasks_to_process = self.check_processed_samples(tasks_to_process)
        logging.info(
            f"Task Processor: {len(tasks_to_process)} tasks need to be processed, {len(skipped_tasks)} tasks are skipped..."
        )

        if multiprocess and tasks_to_process:
            process_count = processes if processes is not None else cpu_count()
            logging.info(f"Using {process_count} processes for task processing.")
            with Pool(processes=process_count) as pool:
                results = pool.starmap(
                    self.process_task, [(task, model) for task in tasks_to_process]
                )
                num_new_tasks = sum(results)
        else:
            logging.info(f"Processing tasks in a single process.")
            for task in tasks_to_process:
                processed = self.process_task(task, model)
                if processed:
                    num_new_tasks += 1

        all_query_responses = self.read_all_query_responses()
        logging.info(
            f"{len(all_query_responses)} tasks in total, {len(skipped_tasks)}"
            f" tasks skipped or already processed, {num_new_tasks} new tasks processed."
        )
        self.write_all_query_responses(all_query_responses)

    def construct_query_data(self, task_item, include_metrics=False):
        task_name = task_item["task_name"]
        query_samples = task_item.get("task_samples", [])

        # Extract global information and example_info from the first sample
        first_sample = query_samples[0]
        global_description = first_sample.get("task_description", "")
        global_images = first_sample.get("global_media", [])
        example_text = first_sample.get("example_text", "")
        example_media = first_sample.get("example_media", [])
        if include_metrics:
            metric_info = first_sample.get("metric_info", {})

        # Verify that task-wise global information and example_info are the same for all samples
        for query in query_samples[1:]:
            if (
                query.get("task_description", "") != global_description
                or query.get("global_media", []) != global_images
                or query.get("example_text", "") != example_text
                or query.get("example_media", []) != example_media
            ):
                raise ValueError(
                    "Global information or example info is not consistent across all samples"
                )
            elif include_metrics and query.get("metric_info", {}) != metric_info:
                raise ValueError("Metric info is not consistent across all samples")

        if isinstance(global_images, str):
            global_images = ast.literal_eval(global_images)
        if isinstance(example_media, str):
            example_media = ast.literal_eval(example_media)

        query_data = {
            "task_name": task_name,
            "global_description": global_description,
            "global_images": global_images,
            "queries": [],
            "example_info": {
                "image_paths": example_media,
                "example_text": example_text,
            },
        }
        if include_metrics:
            query_data["metric_info"] = ast.literal_eval(metric_info)

        for query_idx, query in enumerate(query_samples):
            query_text = query.get("query_text", "")
            query_media = query.get("query_media", [])
            query_answer = ast.literal_eval(query.get("answer", ""))
            global_idx = query.get("id", "")
            if isinstance(query_media, str):
                query_media = ast.literal_eval(query_media)

            query_data["queries"].append(
                {
                    "global_idx": global_idx,
                    "task_idx": query_idx,
                    "image_paths": query_media,
                    "query_text": query_text,
                    "query_answer": query_answer,
                }
            )

        return query_data
