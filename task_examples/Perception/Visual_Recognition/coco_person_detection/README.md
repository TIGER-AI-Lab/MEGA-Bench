# Task: coco_person_detection

## Task Description:

```
You are asked to detect persons in a query image. The format of bounding box is (x1,y1,x2,y2), where (x1,y1) is the top-left corner and (x2,y2) is the bottom-right corner. The coordinates are normalized by the image's height and width, and each value has two significant digits. The boxes are sorted from left to right, then top to bottom.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](000000006954.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'number of person': '5', 'bounding boxes': '[(0.0,0.22,0.25,0.94), (0.23,0.28,0.42,0.69), (0.31,0.26,0.58,0.78), (0.56,0.24,1.0,0.80), (0.57,0.31,0.70,0.66)]'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1124
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Visual_Recognition
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'number of person': 'exact_str_match', 'bounding boxes': 'nbbox_iou_tuple'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'number of person': 1, 'bounding boxes': 1}}
  - **Response Parse Function**: json
