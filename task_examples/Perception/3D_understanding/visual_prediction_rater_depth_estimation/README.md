# Task: visual_prediction_rater_depth_estimation

## Task Description:

```
Depth estimation is an important visual ability. Your task is to understand the accuracy of monocular depth estimation. Given an input image and a list of monocular depth estimation results, you should sort the quality of results from the best to the worst. You should judge the quality based on consistency with input image, alignments with commonsense of distance, and clarity for fine-grained details.

The first image of each query is the input, and the remaining images are the results. Your answer should be a sequence of index. The first result has index 1. Do not count the input image when sorting the results.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](e1-input.png)

![Image](e1-result-metric3d.png)

![Image](e1-result-omnidata.png)

```
Example Question: Red means far, blue means close.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1, 2
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4764
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;3D_understanding
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'order': 'sequence_accuracy_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'order': 1}}
  - **Response Parse Function**: answer_string
