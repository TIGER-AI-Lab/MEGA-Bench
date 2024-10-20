# Task: animal_pose_estimation

## Task Description:

```
This task involves analyzing images to detect and locate 17 animal body keypoints, including eyes, nose, neck, shoulders, elbows, paws, hips, knees, and the root of the tail. The goal is to identify the positions of these keypoints by providing their normalized coordinates within each image. If a keypoint is not visible in the image, it is represented as [0.0, 0.0]. The keypoints are provided in the following order: [0] Left Eye, [1] Right Eye, [2] Nose, [3] Neck, [4] Root of Tail, [5] Left Shoulder, [6] Left Elbow, [7] Left Front Paw, [8] Right Shoulder, [9] Right Elbow, [10] Right Front Paw, [11] Left Hip, [12] Left Knee, [13] Left Back Paw, [14] Right Hip, [15] Right Knee, [16] Right Back Paw. All keypoints are in [x, y] format, and the coordinates are normalized to be within [0, 1] based on the width and height of the image. Your output will be a sequence of 17 such [x, y] coordinates.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](000000000222.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: [[0.26,0.35], [0.0,0.0], [0.26,0.42], [0.4,0.42], [0.77,0.33], [0.45,0.54], [0.45,0.64], [0.42,0.81], [0.56,0.53], [0.6,0.64], [0.66,0.77], [0.7,0.51], [0.78,0.59], [0.77,0.79], [0.77,0.48], [0.83,0.54], [0.83,0.76]]
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1871
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Visual_Recognition
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'sequence_coords_similarity'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
