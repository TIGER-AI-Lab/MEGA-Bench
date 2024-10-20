# Task: av_view_identification

## Task Description:

```
The six multi-view images are captured by cameras mounted on an autonomous-driving vehicle. The task is to determine the view for each image, corresponding to one of the following: back, back_left, back_right, front, front_left, or front_right. The output should specify the view for each image in a sequence, starting from the first image and continuing in order through the final image.
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

![Image](0_4.png)

![Image](0_5.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: front_left, back_right, front_right, back_left, front, back
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1828
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;3D_understanding
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'view_oder': 'sequence_accuracy_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'view_oder': 1}}
  - **Response Parse Function**: answer_string
