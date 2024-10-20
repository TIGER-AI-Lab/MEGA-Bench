# Task: face_keypoint_detection

## Task Description:

```
This task involves analyzing images to detect and locate 5 specific facial landmarks: the **left eye center**, **right eye center**, **nose tip**, **left mouth corner**, and **right mouth corner**. The goal is to accurately identify the positions of these key facial features by providing the normalized coordinates of these keypoints within each image. Each keypoint is [x, y], where x and y are the coordinates normalized based on the width and height and the picture. The output should be a sequence of 5 keypoint coordinates.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: [[0.38,0.52], [0.62,0.51], [0.52,0.62], [0.38,0.7], [0.6,0.68]]
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 191
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Visual_Recognition
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'sequence_coords_similarity'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
