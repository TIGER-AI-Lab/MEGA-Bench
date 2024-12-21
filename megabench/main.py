import argparse
import logging
from pathlib import Path
from task_processor import TaskProcessor
from evaluation_processor import EvaluationProcessor
from utils import prepare_megabench_data

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Mega-Bench Benchmark")
    parser.add_argument(
        "--model_type",
        type=str,
        default="GPT_4O_MINI",
        help="Model type to use for processing tasks.",
    )
    parser.add_argument(
        "--model_path",
        type=str,
        default=None,
        help="Model path, if specified, use this rather than the model type when instantiating a model.",
    )
    parser.add_argument(
        "--ngpus",
        type=int,
        default=None,
        help="Number of GPUs, if specify, it will be passed to the model as additional parameter if specified",
    )
    parser.add_argument(
        "--gpu_utils",
        type=float,
        default=None,
        help="GPU memory utilization, it will be passed to the model as additional parameter if specified",
    )
    parser.add_argument("--output_file", type=str, default="./all_query_responses.json")
    parser.add_argument(
        "--output_score_filename", type=str, default="data_with_scores.json"
    )
    parser.add_argument(
        "--task_name",
        type=str,
        help="Name of the single task folder to process. If not provided, all tasks will be processed.",
        default=None,
    )
    parser.add_argument(
        "--force_regenerate",
        action="store_true",
        help="Whether to force the model to regenerate an answer.",
    )
    parser.add_argument(
        "--query_only",
        action="store_true",
        help="If set, only the query will be performed.",
    )
    parser.add_argument(
        "--evaluation_only",
        action="store_true",
        help="If set, only the evaluation will be performed.",
    )
    parser.add_argument(
        "--force_eval_rule_tasks",
        action="store_true",
        help="If set, rule tasks will always be re-evaluated even if there are already scores in the score output file.",
    )
    parser.add_argument(
        "--multiprocess",
        action="store_true",
        help="If set, tasks will be processed using multiple processes.",
    )
    parser.add_argument(
        "--processes",
        type=int,
        default=2,
        help="Number of processes to use if multiprocessing is enabled. If not set, it defaults to the number of CPU cores.",
    )
    parser.add_argument(
        "--print_response",
        action="store_true",
        help="Print every response of task.",
    )
    parser.add_argument(
        "--dataset_name",
        type=str,
        default="TIGER-Lab/MEGA-Bench",
    )
    parser.add_argument(
        "--dataset_subset_name",
        type=str,
        choices=["core", "open", "core_single_image", "open_single_image"],
        default="core",
    )

    args = parser.parse_args()
    logger.info(f"Arguments: {args}")

    # Load HF datasets
    subset_dataset, all_dataset = prepare_megabench_data(args.dataset_name, args.dataset_subset_name)

    if not args.evaluation_only:
        additional_args = {}
        if args.ngpus:
            additional_args["ngpus"] = args.ngpus
        if args.gpu_utils:
            additional_args["gpu_utils"] = args.gpu_utils

        output_file_dir = Path(args.output_file).parent
        output_file_dir.mkdir(parents=True, exist_ok=True)

        task_processor = TaskProcessor(
            output_file=args.output_file,
            model_type=args.model_type,
            print_response=args.print_response,
            model_path=args.model_path,
            force_regenerate=args.force_regenerate,
            **additional_args,
        )
        task_processor.process_all_tasks(
            single_task_name=args.task_name,
            multiprocess=args.multiprocess,
            processes=args.processes,
            data=subset_dataset,
        )

    if not args.query_only:
        result_base = Path(args.output_file).parent
        output_score_file = result_base / args.output_score_filename

        eval_log_file = result_base / "evaluation_logs.txt"
        sanity_check_eval = args.model_type == "GROUND_TRUTH_ORACLE_SANITY_CHECK"
        # Score the model's responses, using the configured metrics
        evaluation_processor = EvaluationProcessor(
            hf_data=all_dataset,
            data_file=args.output_file,
            logging_file=eval_log_file,
            output_score_file=output_score_file,
            sanity_check_eval=sanity_check_eval,
            force_eval_rule_tasks=args.force_eval_rule_tasks,
        )
        evaluation_processor.process(single_task_name=args.task_name)
