# MEGA-Bench: Scaling Multimodal Evaluation to over 500 Real-World Tasks

[![arXiv](https://img.shields.io/badge/arXiv-2410.10563-b31b1b.svg)](https://arxiv.org/abs/2410.10563)
[![Project Page](https://img.shields.io/badge/Project-Page-blue)](https://tiger-ai-lab.github.io/MEGA-Bench/)
[![Dataset](https://img.shields.io/badge/🤗-Dataset-yellow)](https://huggingface.co/datasets/TIGER-Lab/MEGA-Bench)
[![Leaderboard](https://img.shields.io/badge/🤗HuggingFace-Space-blue)](https://huggingface.co/spaces/TIGER-Lab/MEGA-Bench)

## 🔔 News

**🔥[2024-10-18]: Data and evaluation code are now available. We will continue to add evaluation pipelines for more models.**

**📄[2024-10-14]: Paper released on arXiv.**

## Table of Contents
1. [Introduction](#introduction)
2. [Setup](#setup)
   - [Dataset Download](#dataset-download)
   - [Environment Setup](#environment-setup)
3. [Evaluation](#evaluation)
   - [Proprietary Models](#proprietary-models-gpt-claude)
   - [Open-source Models](#open-source-models-qwen2vl-internvl2)
   - [Detailed explanation of command line arguments](#detailed-explanation-of-command-line-arguments)
4. [Contact and Citation](#contact-and-citation)

## Introduction

MEGA-Bench is an evaluation suite that scales multimodal evaluation to over 500 real-world tasks, addressing the highly heterogeneous daily use cases of end users. Our objective is to optimize for a set of high-quality data samples that cover a diverse and rich set of multimodal tasks while enabling cost-effective and accurate model evaluation.

![MEGA-Bench Taxonomy Tree](resources/mega-bench-taxonomy_tree.png)

Key features of MEGA-Bench:

- 505 realistic tasks encompassing over 8,000 samples from 16 expert annotators
- Wide range of output formats including numbers, phrases, code, LaTeX, coordinates, JSON, free-form, etc.
- Over 40 metrics developed to evaluate these diverse tasks
- Fine-grained capability report across multiple dimensions (e.g., application, input type, output format, skill)
- Interactive visualization of model capabilities

Unlike existing benchmarks that unify problems into standard multi-choice questions, MEGA-Bench embraces the diversity of real-world tasks and their output formats. This allows for a more comprehensive evaluation of vision-language models across various dimensions.

## Setup

Clone the repository by:

```bash
# Clone the repository with the task examples
git clone https://github.com/TIGER-AI-Lab/MEGA-Bench.git
# Or skip the task examples host by Git LFS
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/TIGER-AI-Lab/MEGA-Bench.git

cd MEGA-Bench
```

### Dataset download

The MEGA-Bench dataset is now available on Hugging Face:

[MEGA-Bench Dataset](https://huggingface.co/datasets/TIGER-Lab/MEGA-Bench)

Since the Hugging Face Datasets viewer does not support visualizing large rows with many images, we chose to only keep the file paths of images/videos in the HF dataset. Please download the data, unzip it, and set up the data path properly using the following commands:

```bash
wget https://huggingface.co/datasets/TIGER-Lab/MEGA-Bench/resolve/main/data.zip?download=true -O data.zip
unzip data.zip -d megabench
```

### Environment Setup

First, set up the environment with the following commands. The packages are mainly for the evaluation metrics used in MEGA-Bench.

```bash
conda create -n megabench python=3.12
conda activate megabench
pip install -r requirements.txt
python -c "import nltk; nltk.download('wordnet'); nltk.download('punkt')"
```


## Evaluation

**📌 Note:** Due to slight reorganization of the prompt for uploading to Hugging Face Datasets, the evaluation results from this repository may differ slightly from those reported in the paper. However, the overall performance trend and capability report should remain consistent.

In the initial release, we provide evaluation pipelines for four types of models: GPT, Claude, Qwen2VL, and InternVL2. See `megabench/models/model_type.py` for details on the model types. We will add code for more models in the future.

### Proprietary Models (GPT, Claude)

To run with GPT or Claude, set up the OpenAI or Anthropic API key:

```bash
export OPENAI_API_KEY=<your_openai_api_key>
export ANTHROPIC_API_KEY=<your_anthropic_api_key>
```

Example commands for running evaluation with GPT-4o (0513) or Claude-3.5-Sonnet on the **Core subset**, using multiprocessing with 2 subprocesses:

```bash
cd megabench

# GPT-4o (0513)
python main.py --model_type GPT_4O_0513 --output_file results/GPT-4o-0513/all_query_responses.json --print_response --dataset_subset_name core --multiprocess --processes 2

# Claude-3.5-Sonnet
python main.py --model_type CLAUDE_3_5_SONNET --output_file results/Claude-3.5-Sonnet/all_query_responses.json --print_response --dataset_subset_name core --multiprocess --processes 2
```

To run with the Open-ended subset, set ```--dataset_subset_name open```. The evaluation processor will evaluate all tasks in the response output file. **If you only want to evaluate the Core subset, you should set different output file paths for Core and Open-ended subsets.**

To evaluate the Open-ended subset, you need to set up the OpenAI API key first.


### Open-source Models (Qwen2VL, InternVL2)

To run with Qwen2VL or InternVL2, first install the latest [vllm](https://github.com/vllm-project/vllm):

```bash
pip install vllm -U
```

Example commands for running evaluation with Qwen2VL or InternVL2 on the **Core subset**, using multiprocessing with 2 subprocesses:

```bash
cd megabench

# InternVL2-8B
python main.py --model_type INTERNVL2_8B \
   --output_file results/InternVL2_8B/all_query_responses.json \
   --print_response --ngpus 4 --gpu_utils 0.9 \
   --dataset_name TIGER-Lab/MEGA-Bench \
   --dataset_subset_name core

# Qwen2VL-7B
python main.py --model_type QWEN2_VL_7B \
   --output_file results/Qwen2_VL_7B/all_query_responses.json \
   --print_response --ngpus 4 --gpu_utils 0.9 \
   --dataset_name TIGER-Lab/MEGA-Bench \
   --dataset_subset_name core
```
If you want to evaluate on the open set, change it to ``--dataset_subset_name open``.


### Ground truth sanity check

Run the ground-truth sanity check with the following command:
```bash
python main.py \
   --model_type GROUND_TRUTH_ORACLE_SANITY_CHECK \
   --output_file results/Ground_truth_oracle_sanity_check/all_query_responses.json \
   --force_regenerate \
   --multiprocess --processes 48 \
   --dataset_name TIGER-Lab/MEGA-Bench \
   --dataset_subset_name core
```
This should produce full scores for the Core tasks, which helps verify the validity of the metric implementations.

### Detailed explanation of command line arguments

The launch script ``main.py`` has the following arguments:

| Argument | Description | Default |
|----------|-------------|---------|
| `--model_type` | Type of model to use | "GPT_4O_MINI" |
| `--model_path` | Custom model path for local open-source models | None |
| `--ngpus` | Number of GPUs to use (for vllm models) | None |
| `--gpu_utils` | GPU memory utilization (0.0 to 1.0, for vllm models) | None |
| `--output_file` | Path for query responses output | None |
| `--output_score_filename` | Filename for evaluation scores | "data_with_scores.json" |
| `--task_name` | Name of a specific task to process, if specified, the pipeline will run only a single task | None |
| `--force_regenerate` | Force regeneration of answers | False |
| `--query_only` | Perform only the model query, without evaluation | False |
| `--evaluation_only` | Perform only the evaluation step | False |
| `--multiprocess` | Enable multiprocessing (for API-based proprietary models) | False |
| `--processes` | Number of processes for multiprocessing | 2 |
| `--print_response` | Print model's response (helpful for debugging) | False |
| `--dataset_name` | Name of the dataset | "TIGER-Lab/MEGA-Bench" |
| `--dataset_subset_name` | Subset of the dataset to use | "core" |


## Contact and Citation

For any questions or concerns, please contact:

- Jiacheng Chen: jcchen.work@gmail.com
- Wenhu Chen: wenhuchen@uwaterloo.ca

If you find this work useful for your research, please consider citing our paper:

```bibtex
@article{chen2024mega-bench,
  title={MEGA-Bench: Scaling Multimodal Evaluation to over 500 Real-World Tasks},
  author={Chen, Jiacheng and Liang, Tianhao and Siu, Sherman and Wang, Zhengqing and Wang, Kai and Wang, Yubo and Ni, Yuansheng and Zhu, Wang and Jiang, Ziyan and Lyu, Bohan and Jiang, Dongfu and He, Xuan and Liu, Yuan and Hu, Hexiang and Yue, Xiang and Chen, Wenhu},
  journal={arXiv preprint arXiv:2410.10563},
  year={2024},
}
```
