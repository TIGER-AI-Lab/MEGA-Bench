from functools import cached_property
import json
import pathlib
import logging
from multiprocessing import Pool, current_process, cpu_count
from filelock import FileLock
from models.model_type import ModelType
import ast
from tqdm import tqdm


class TaskProcessor:
    """MEGA-Bench task processor, generate model responses to get ready for evaluation.
    
    This task processor handles:
    1. Managing output files for task responses
    2. Checking task/sample completion status
    3. Preparing query data for models
    4. Executing task processing with models
    
    Attributes:
        output_file (str): Path to the JSON file storing task responses
        model_type (ModelType): Type of model to use for processing
        print_response (bool): Whether to print model responses
        model_path (str): Path to local model if applicable
        force_regenerate (bool): Whether to force regeneration of all responses
        api_error_patterns (list): Patterns to identify API-related errors. Those samples will be re-run
    """

    def __init__(
        self,
        output_file,
        model_type,
        print_response=False,
        model_path=None,
        force_regenerate=False,
        **kwargs,
    ):
        """Initialize the TaskProcessor.
        
        Args:
            output_file (str): Path to output JSON file
            model_type (str): Type of model to use
            print_response (bool, optional): Print model responses. Defaults to False.
            model_path (str, optional): Path to local model. Defaults to None.
            force_regenerate (bool, optional): Force regenerate all responses. Defaults to False.
            **kwargs: Additional model-specific arguments
        """
        self.output_file = output_file
        self.model_type = ModelType.from_string(model_type)
        self.print_response = print_response
        self.model_path = model_path
        self.force_regenerate = force_regenerate
        self.model_kwargs = kwargs
        self.init_output_file_exists()
        self.api_error_patterns = [
            "API quota exceeded",
            "rate limit exceeded",
            "quota exceeded",
            "API limit reached",
        ]

    # 1. Output File Management
    @cached_property
    def output_path(self) -> pathlib.Path:
        """Get the path to the output file."""
        return pathlib.Path(self.output_file)

    def read_all_query_responses(self):
        """Read all query responses from the output file."""
        if self.output_path.exists():
            with self.output_path.open("r", encoding="utf-8") as file:
                return json.load(file)
        return []

    def write_all_query_responses(self, all_query_responses):
        """Write query responses to the output file."""
        with self.output_path.open("w", encoding="utf-8") as f:
            json.dump(all_query_responses, f, ensure_ascii=False, indent=4)

    def init_output_file_exists(self):
        """Initialize output file if it doesn't exist."""
        if not self.output_path.exists():
            self.write_all_query_responses([])
    
    def update_prev_query_response(self, all_query_responses, updated_prev_task_results):
        """Update previous query responses with new results."""
        updated_all_query_responses = []
        for idx in range(len(all_query_responses)):
            task_name = all_query_responses[idx]["task_name"]
            if task_name in updated_prev_task_results:
                if updated_prev_task_results[task_name] is not None:
                    updated_all_query_responses.append(updated_prev_task_results[task_name])
            else:
                updated_all_query_responses.append(all_query_responses[idx])

        self.write_all_query_responses(all_query_responses)

    def append_query_response(self, response_data, samples_to_run):
        """Append or update specific samples in the response file."""
        lock_path = self.output_path.with_suffix(".lock")
        with FileLock(lock_path):
            all_query_responses = self.read_all_query_responses()
            task_name = response_data["task_name"]

            # Find existing task
            task_found = False
            for task in all_query_responses:
                if task["task_name"] == task_name:
                    task_found = True

                    # Update global info
                    task["global_description"] = response_data["global_description"]
                    task["global_images"] = response_data["global_images"]
                    task["example_info"] = response_data["example_info"]

                    # Remove old responses for the samples we're updating
                    task["query_response"] = [
                        resp
                        for resp in task["query_response"]
                        if resp.get("query_idx") not in samples_to_run
                    ]

                    # Add new responses
                    task["query_response"].extend(response_data["query_response"])
                    break

            # If task not found, create new entry
            if not task_found:
                new_task = {
                    "task_name": task_name,
                    "global_description": response_data["global_description"],
                    "global_images": response_data["global_images"],
                    "example_info": response_data["example_info"],
                    "query_response": response_data["query_response"],
                }
                all_query_responses.append(new_task)

            self.write_all_query_responses(all_query_responses)

    # 2. Task/Sample Status Checking
    def did_global_info_change(self, perv_response, task_data):
        """Check if task's global information has changed."""
        if perv_response["global_description"] != task_data["global_description"]:
            logging.debug(
                f'Global description changed. {perv_response["global_description"]=}, {task_data["global_description"]=}'
            )
            return True
        if perv_response["global_images"] != task_data["global_images"]:
            logging.debug(
                f'Global images changed. {perv_response["global_images"]=}, {task_data["global_images"]=}'
            )
            return True
        return False

    def is_api_error_response(self, response):
        """Check if a response contains API-related errors."""
        if not isinstance(response, str):
            return False
        return any(
            pattern.lower() in response.lower() for pattern in self.api_error_patterns
        )

    def did_sample_change(self, prev_response, query_info):
        """Check if a sample's content has changed."""
        prev_sample = {
            "image_paths": prev_response.get("images", []),
            "query_text": prev_response.get("query_text", ""),
        }
        new_sample = {
            "image_paths": query_info.get("image_paths", []),
            "query_text": query_info.get("query_text", ""),
        }
        return str(prev_sample) != str(new_sample)

    def update_sample_ground_truth_inplace(self, prev_response, query_info):
        """Update ground truth for a sample if needed."""
        correct_answer = query_info["correct_answer"]
        if str(prev_response.get("correct_answer")) != str(correct_answer):
            logging.debug("Detect annotation change!")
            logging.debug("Latest answer from annotation:", correct_answer)
            logging.debug(
                "Old answer from output file:", prev_response.get("correct_answer")
            )
            prev_response["correct_answer"] = correct_answer
            return True
        return False

    def _verify_task_completeness(self, task_name, task_data, prev_task_results=None):
        """Check which samples need to be processed for a task.

        Returns:
            tuple: (is_task_complete, samples_to_run)
                - is_task_complete: bool indicating if all samples are up-to-date
                - samples_to_run: list of indices that need to be processed
        """
        samples_to_run = []

        # If task doesn't exist, run all samples
        if prev_task_results is None:
            return False, list(range(len(task_data["queries"]))), None

        # Check if global content changed or need to force regenerate
        # Re-run all samples if global content changed
        if self.did_global_info_change(prev_task_results, task_data):
            logging.info(f"Global content changed for task {task_name}")
            return False, list(range(len(task_data["queries"]))), None
        elif self.force_regenerate:
            logging.info(f"Force regenerate is enabled for task {task_name}")
            return False, list(range(len(task_data["queries"]))), None

        # There are previous responses, check if any of them need to be re-run
        prev_responses_mapping = {}
        for prev_resp_idx, prev_response in enumerate(
            prev_task_results["query_response"]
        ):
            prev_responses_mapping[prev_response["query_idx"]] = (
                prev_resp_idx,
                prev_response,
            )

        # Check each sample
        for query_info in task_data["queries"]:
            should_rerun = False
            query_idx = query_info["query_idx"]

            # Check if sample exists
            if query_idx not in prev_responses_mapping:
                should_rerun = True
            else:
                prev_resp_idx, prev_response = prev_responses_mapping[query_idx]

                # Check for API errors
                if self.is_api_error_response(prev_response["response"]):
                    logging.warning(
                        f"API error detected for task {task_name} sample {query_idx}, will rerun..."
                    )
                    should_rerun = True
                # Check if sample content changed
                elif self.did_sample_change(prev_response, query_info):
                    logging.warning(
                        f"Sample content changed for task {task_name} sample {query_idx}, will rerun..."
                    )
                    should_rerun = True
                # Update ground truth if needed, no need to rerun
                else:
                    self.update_sample_ground_truth_inplace(prev_response, query_info)

            if should_rerun:
                samples_to_run.append(query_idx)
        
        # If any samples need to be run, update the task results
        if samples_to_run:
            # Remove responses for samples that will be re-run
            prev_task_results["query_response"] = [
                resp
                for resp in prev_task_results["query_response"]
                if resp['query_idx'] not in samples_to_run
            ]
            return False, samples_to_run, prev_task_results

        return True, [], prev_task_results

    def verify_task_completeness(self, task, prev_task_results):
        """Verify task completion status and identify samples to process."""
        task_name = task["task_name"]
        task_data = self.prepare_query_data(task)

        is_task_complete, samples_to_run, prev_task_results = (
            self._verify_task_completeness(task_name, task_data, prev_task_results)
        )
        return is_task_complete, samples_to_run, prev_task_results

    def check_processed_samples(self, tasks):
        """Check which samples need processing across all tasks."""
        print("Checking processed samples...")
        with open(self.output_path, "r", encoding="utf-8") as f:
            all_query_responses = json.load(f)
        
        prev_task_results_mapping = {}
        for prev_task in all_query_responses:
            prev_task_results_mapping[prev_task["task_name"]] = prev_task

        results = []
        for task in tqdm(tasks, desc="Check task completeness"):
            prev_task_results = prev_task_results_mapping.get(task["task_name"], None)
            results.append(self.verify_task_completeness(task, prev_task_results))

        # Update the previous task response results
        updated_prev_task_results = {}
        for task, (is_task_complete, samples_to_run, prev_task_results) in zip(tasks, results):
            task["samples_to_run"] = samples_to_run
            task["is_task_complete"] = is_task_complete
            updated_prev_task_results[task["task_name"]] = prev_task_results
        self.update_prev_query_response(all_query_responses, updated_prev_task_results)

        num_total_samples = sum([len(task["task_samples"]) for task in tasks])
        num_to_process_samples = sum([len(task["samples_to_run"]) for task in tasks])

        skipped = [task for task in tasks if task["is_task_complete"]]
        to_be_processed = [task for task in tasks if not task["is_task_complete"]]

        logging.info(
            f"Task Processor: {len(to_be_processed)} tasks need to be processed, {len(skipped)} tasks are skipped..."
        )
        logging.info(
            f"Task Processor: {num_to_process_samples} samples need to be processed, {num_total_samples - num_to_process_samples} samples are skipped..."
        )

        return skipped, to_be_processed
    
    # 3. Query Data Preparation
    def prepare_query_data(self, task_item, include_metrics=False):
        """Prepare query data for model processing.
        
        Args:
            task_item (dict): Task information including samples
            include_metrics (bool): Whether to include evaluation metrics, only used 
            for the GROUND_TRUTH_ORACLE_SANITY_CHECK model

        Returns:
            dict: Structured query data for model processing
        """
        task_name = task_item["task_name"]
        samples = task_item.get("task_samples", [])

        # Extract global information and example_info from the first sample
        first_sample = samples[0]
        global_description = first_sample.get("task_description", "")
        global_images = first_sample.get("global_media", [])
        example_text = first_sample.get("example_text", "")
        example_media = first_sample.get("example_media", [])
        if include_metrics:
            metric_info = first_sample.get("metric_info", {})

        # Verify that task-wise global information and example_info are the same for all samples
        for query in samples[1:]:
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

        for query_idx, query in enumerate(samples):
            query_text = query.get("query_text", "")
            query_media = query.get("query_media", [])
            correct_answer = ast.literal_eval(query.get("answer", ""))
            global_idx = query.get("id", "")
            if isinstance(query_media, str):
                query_media = ast.literal_eval(query_media)

            query_data["queries"].append(
                {
                    "global_idx": global_idx,
                    "query_idx": query_idx,
                    "image_paths": query_media,
                    "query_text": query_text,
                    "correct_answer": correct_answer,
                }
            )

        return query_data
    
    def augment_response_with_task_info(self, task_name, task_data, query_response):
        """Augment model responses with task information, used for evaluation.
        
        Args:
            task_name (str): Name of the task
            task_data (dict): Task data including queries
            query_response (list): Model responses to augment
        """
        assert len(query_response) == len(task_data["queries"])
        for i, query in enumerate(query_response):
            query["global_idx"] = task_data["queries"][i]["global_idx"]
            query["query_idx"] = task_data["queries"][i]["query_idx"]
            query["images"] = task_data["queries"][i]["image_paths"]
            query["query_text"] = task_data["queries"][i]["query_text"]

        return {
            "task_name": task_name,
            "global_description": task_data["global_description"],
            "global_images": task_data["global_images"],
            "example_info": task_data["example_info"],
            "query_response": query_response,
        }
    
    # 4. Task Processing
    def process_task(self, task_item, model=None) -> bool:
        """Process a single task with specified samples.
        
        Args:
            task_item (dict): Task to process including samples_to_run
            model: Model instance to use for processing
        """

        if model is None:
            model = self.model_type.get_model_instance(
                print_response=self.print_response,
                model_path=self.model_path,
                **self.model_kwargs,
            )

        task_name = task_item["task_name"]
        samples_to_run = task_item["samples_to_run"]
        include_metrics = (
            True
            if self.model_type == ModelType.GROUND_TRUTH_ORACLE_SANITY_CHECK
            else False
        )
        task_data = self.prepare_query_data(task_item, include_metrics)

        logging.info(
            f"Processing {task_name} - {len(samples_to_run)}/{len(task_data['queries'])} samples to be processed..."
        )
        task_data["queries"] = [task_data["queries"][i] for i in samples_to_run]

        process_id = (
            current_process()._identity[0] if current_process()._identity else 0
        )
        query_response = model.query(
            task_name=task_name, query_data=task_data, position=process_id
        )

        query_response = self.augment_response_with_task_info(
            task_name, task_data, query_response
        )
        self.append_query_response(query_response, samples_to_run)

        return True

    def process_all_tasks(
        self, single_task_name=None, processes=None, multiprocess=True, data=None
    ):
        """Process multiple tasks with optional multiprocessing.
        
        Args:
            single_task_name (str, optional): Process only this task. Defaults to None.
            processes (int, optional): Number of processes to use. Defaults to None.
            multiprocess (bool, optional): Use multiprocessing. Defaults to True.
            data (list, optional): Task data to process. Defaults to None.
        """
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
        if "KEY" in self.model_type.api_key:
            model = None
        else:
            model = self.model_type.get_model_instance(
                print_response=self.print_response,
                model_path=self.model_path,
                **self.model_kwargs,
            )

        skipped_tasks, tasks_to_process = self.check_processed_samples(tasks_to_process)

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
            f"{len(all_query_responses)} tasks in total in the output file, {len(skipped_tasks)}"
            f" tasks skipped or already processed, {num_new_tasks} new tasks processed."
        )
