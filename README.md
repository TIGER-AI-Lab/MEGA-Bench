# MEGA-Bench: Scaling Multimodal Evaluation to over 500 Real-World Tasks

[![arXiv](https://img.shields.io/badge/arXiv-2410.10563-b31b1b.svg)](https://arxiv.org/abs/2410.10563)
[![Project Page](https://img.shields.io/badge/Project-Page-blue)](https://tiger-ai-lab.github.io/MEGA-Bench/)
[![Dataset](https://img.shields.io/badge/🤗-Dataset-yellow)](https://huggingface.co/datasets/TIGER-Lab/MEGA-Bench)

## 🔔 News

**🔥[2024-10-14]: Paper released on arXiv. Data and evaluation code will be released soon.**

## Introduction

We present MEGA-Bench, an evaluation suite that scales multimodal evaluation to over 500 real-world tasks, to address the highly heterogeneous daily use cases of end users. Our objective is to optimize for a set of high-quality data samples that cover a highly diverse and rich set of multimodal tasks, while enabling cost-effective and accurate model evaluation.

![MEGA-Bench Taxonomy Tree](resources/mega-bench-taxonomy_tree.png)

Key features of MEGA-Bench:

- 505 realistic tasks encompassing over 8,000 samples from 16 expert annotators
- Wide range of output formats including numbers, phrases, code, LaTeX, coordinates, JSON, free-form, etc.
- Over 40 metrics developed to evaluate these diverse tasks
- Fine-grained capability report across multiple dimensions (e.g., application, input type, output format, skill)
- Interactive visualization of model capabilities

Unlike existing benchmarks that unify problems into standard multi-choice questions, MEGA-Bench embraces the diversity of real-world tasks and their output formats. This allows for a more comprehensive evaluation of vision-language models across various dimensions.

## Dataset

The MEGA-Bench dataset is now available on the Hugging Face. You can access it at:

[MEGA-Bench](https://huggingface.co/datasets/TIGER-Lab/MEGA-Bench)

## Evaluation

[Evaluation code and instructions will be added once released]

## Contact

For any questions or concerns, please contact:

- Jiacheng Chen: jcchen.work@gmail.com
- Wenhu Chen: wenhuchen@uwaterloo.ca

## Citation

If you find this work useful for your research, please consider citing our paper:

```bibtex
@article{chen2024mega-bench,
  title={MEGA-Bench: Scaling Multimodal Evaluation to over 500 Real-World Tasks},
  author={Chen, Jiacheng and Liang, Tianhao and Siu, Sherman and Wang, Zhengqing and Wang, Kai and Wang, Yubo and Ni, Yuansheng and Zhu, Wang and Jiang, Ziyan and Lyu, Bohan and Jiang, Dongfu and He, Xuan and Liu, Yuan and Hu, Hexiang and Yue, Xiang and Chen, Wenhu},
  journal={arXiv preprint arXiv:2410.10563},
  year={2024},
}
```