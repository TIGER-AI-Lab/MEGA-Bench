# Task: coco_object_detection_by_query_property

## Task Description:

```
Given a query image and a description of object's property, you are required to detect the bounding box of all objects that have the specified property. The format of bounding box is (x1,y1,x2,y2), where (x1,y1) is the top-left corner and (x2,y2) is the bottom-right corner. The coordinates are normalized by the image's height and width, and each value has two significant digits. If there are multiple objects, the boxes are sorted from left to right, then top to bottom.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](000000077396.png)

```
Example Question: The object's category is cat
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'number of objects': '2', 'bounding boxes': '[(0.14,0.72,0.41,1,0), (0.36,0.42,0.61,0.76)]'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 763
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Visual_Recognition
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'number of objects': 'exact_str_match', 'bounding boxes': 'nbbox_iou_tuple'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'number of objects': 1, 'bounding boxes': 1}}
  - **Response Parse Function**: json
