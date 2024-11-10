import json
import argparse
from pathlib import Path
from analysis_utils import (
    task_list_refine,
    collect_task_metadata,
    derive_keyword_stats,
)

def merge_json_files(input_dir, output_path, key="name"):
    """
    Merge multiple JSON files containing evaluation results from a directory.
    Looks for all files matching pattern 'data_with_scores*.json'.
    Prioritizes LLM evaluations over rule-based ones when duplicates exist.
    """
    data_dict = {}  # Using name as key for easy lookup and updates
    
    # Find all matching JSON files in the directory
    json_paths = list(Path(input_dir).glob("data_with_scores*.json"))
    print(f"Found {len(json_paths)} files to merge")
    
    # Load and merge all JSON files
    for path in json_paths:
        print(f"Processing {path}")
        with open(path, "r") as f:
            data = json.load(f)
            if isinstance(data, dict) and "data" in data:
                data = task_list_refine(data["data"])
            
            # Update or add entries
            for item in data:
                item_key = item[key]
                # If new item or if new item is LLM-evaluated (prioritize LLM eval)
                if item_key not in data_dict or (
                    item.get("eval_type") == "llm" and data_dict[item_key].get("eval_type") != "llm"
                ):
                    data_dict[item_key] = item

    # Convert back to list
    merged_data = list(data_dict.values())
    
    # Save the merged result
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(merged_data, f, indent=4)
    
    print(f"Merged file with {len(merged_data)} tasks saved to {output_path}")
    return merged_data

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Merge and process evaluation score files.')
    parser.add_argument('input_dir', type=str, help='Directory containing score files')
    args = parser.parse_args()

    # Convert path to Path object
    input_dir = Path(args.input_dir)
    
    # Create analysis directory under input directory
    output_dir = input_dir / "analysis"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Merge files
    output_path = output_dir / "merged_results.json"
    merged_data = merge_json_files(input_dir, output_path)
    
    # Collect metadata and derive keyword stats
    task_metadata = collect_task_metadata(merged_data, all_task_meta_path="all_task_meta.json")
    keyword_stats = derive_keyword_stats(task_metadata)
    
    # Save keyword stats
    stats_output = output_dir / "multi_dim_keyword_stats.json"
    with open(stats_output, "w") as f:
        json.dump(keyword_stats, f, indent=4)
    
    print(f"\nResults saved in {output_dir}:")
    print(f"- Merged data: {output_path}")
    print(f"- Multi-dimensional keywords stats: {stats_output}")

if __name__ == "__main__":
    main()