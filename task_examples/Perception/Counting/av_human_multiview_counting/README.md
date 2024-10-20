# Task: av_human_multiview_counting

## Task Description:

```
The six multi-view images are captured from cameras mounted on the car: back, back-left, back-right, front, front-left, and front-right. Your task is to count the number of unique humans within the bounding box across these images based on proper 3d reasoning. Do not count the same human multiple time
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0_CAM_BACK.png)

![Image](0_CAM_BACK_LEFT.png)

![Image](0_CAM_BACK_RIGHT.png)

![Image](0_CAM_FRONT.png)

![Image](0_CAM_FRONT_LEFT.png)

![Image](0_CAM_FRONT_RIGHT.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 3
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 69
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Counting
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'humans': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'humans': 1}}
  - **Response Parse Function**: answer_string
