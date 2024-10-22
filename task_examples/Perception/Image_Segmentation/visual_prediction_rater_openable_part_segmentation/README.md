# Task: Visual prediction rater openable part segmentation

## Task Description:

```
Openable part segmentation is crucial for interacting with the environment and your task is to understand the quality of openable part segmentation. Several openable part segmentation results are presented; you should rank them from the best to the worst. When comparing different results, please consider 1) consistency with the input image, 2) correct identification of the openable attribute, and 3) precise boundaries.

The first image is the input; the rest are the results. Rank the results using their indices, starting with 1. Exclude the input image from the ranking.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0_0.png)

![Image](0_1.png)

![Image](0_2.png)

![Image](0_3.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1, 2, 3
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4720
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Image_Segmentation
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'order': 'sequence_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'order': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were collected using screenshots from arXiv papers' qualitative results. Questions and answers were created by the annotator
