# Task: Visual prediction rater surface normal estimation

## Task Description:

```
Surface normal estimation is an important visual ability. Your task is to understand the accuracy of surface normal estimation. Given an input image followed by a list of surface normal estimation results, you should sort the quality of results from the best to the worst. You should judge the quality based on consistency with input image, alignments with commonsense of 3D world, and clarity for fine-grained details. Note that the color encoding in the results represents the direction of surface normal.

The first image of each query is the input, and the remaining images are the results. Your answer should be a sequence of index. The first result has index 1. Do not count the index of input image in your output.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1-input.png)

![Image](1-result-1.png)

![Image](1-result-2.png)

![Image](1-result-3.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1, 3, 2
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4706
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;3D_understanding
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'order': 'sequence_accuracy_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'order': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were collected by taking screenshots from surface normal estimation papers on arXiv. Questions and answers were created by the annotator
