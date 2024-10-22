# Task: 3d indoor scene text bbox prediction

## Task Description:

```
The given image is a 2D projection of a 3D scene with color. The task is to find the 2D bounding box within the image that corresponds to a specific object described by a text query. The format of bounding box is (x1,y1,x2,y2), where (x1,y1) is the top-left corner and (x2,y2) is the bottom-right corner. The coordinates are normalized by the image's height and width, and each value has three significant digits.
```

![Image](scene0000.png)

## The 1-shot Example for Task Demonstration:

## Example Query:

```
Question: A white cabinet in the corner of the room. in the direction from the door and from the inside. it will be on the left, there is a small brown table on the left side of the cabinet and a smaller table on the right side of the cabinet.
```

```
Demonstration example(s) of the task:
Example 1:
Example Question: A black tv, in the direction from the entrance and from the outside, will be on the right side of the blue curtain . on the left of the tv is a small bike.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: (0.64, 0.21, 0.75, 0.31)
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1040
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;3D_understanding
- **Application**: Perception
- **Input Format**: 3D Models and Aerial Imagery
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'bounding boxes': 'nbbox_iou_single'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'bounding boxes': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: The data is adapted from Multi3DRefer. Questions and answers were designed by the annotator and dataset annotation.
