# Task: visual_prediction_rater_3d_assembled_quality_understanding

## Task Description:

```
This task involves ranking the quality of three different assembled results. Each image shows a final object assembled from fragments, with different colors representing different fragments. Your goal is to evaluate and rank the quality of these assemblies.

The images are indexed from left to right as 1, 2, and 3. Rank the results using these indices.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](00.png)

![Image](01.png)

![Image](02.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1, 2, 3
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4734
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;3D_understanding
- **App**: Perception
- **Input Format**: 3D Models and Aerial Imagery
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Order': 'sequence_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Order': 1}}
  - **Response Parse Function**: answer_string
