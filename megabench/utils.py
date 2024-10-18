import importlib
from mimetypes import guess_type


def lazy_import(module_name, class_name):
    """Import the module lazily."""

    def importer():
        module = importlib.import_module(module_name)
        return getattr(module, class_name)

    return importer


def is_video_file(file_path):
    mime_type, _ = guess_type(file_path)
    if not mime_type:
        return False
    return mime_type.startswith("video")



def organize_hf_dataset(dataset):
    """
    Organize the dataset with task-based manner

    Return:
        organized_dataset: list, each item is a dict, with the following keys:
            - task_name: str
            - task_query_samples: list of dicts, each dict contains the sample information
    """
    task_dict = {}
    for sample in dataset:
        task_name = sample["task_name"]
        if task_name not in task_dict:
            task_dict[task_name] = []
        task_dict[task_name].append(sample)
    
    organized_dataset = []
    for task_name, samples in task_dict.items():
        organized_dataset.append({
            "task_name": task_name,
            "task_samples": samples
        })
    
    return organized_dataset
    