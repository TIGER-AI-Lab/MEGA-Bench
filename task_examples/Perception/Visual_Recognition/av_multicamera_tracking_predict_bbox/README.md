# Task: av_multicamera_tracking_predict_bbox

## Task Description:

```
The task is to track a single car across multiple frames, from the viewpoint of an autonomous-driving car with multiple mounted cameras. In the first frame, the car is highlighted by a blue bounding box. The goal is to track the same car and output the bounding box coordinates in each subsequent frames (excluding the first frame). Note that the image of each frame can come from different cameras. The output format should be a list of tuples: [(x1, y1, x2, y2), (x1, y1, x2, y2), ...], where (x1, y1) is the top-left corner and (x2, y2) is the bottom-right corner. The output bounding box coordinates should be normalized with respect to the width and height, falling between 0 and 1, and rounded to two significant digits. There should be one box per frame.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](7_init.png)

![Image](7_1.png)

![Image](7_2.png)

![Image](7_3.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: [(0.66, 0.52, 0.92, 0.71), (0.16, 0.54, 0.25, 0.62), (0.30, 0.55, 0.35, 0.60)]
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1300
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Visual_Recognition
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'bbox sequence': 'nbbox_iou_sequence'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'bbox sequence': 1}}
  - **Response Parse Function**: answer_string
