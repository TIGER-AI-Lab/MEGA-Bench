# Task: Single person pose estimation

## Task Description:

```
This task involves analyzing images to detect and locate 17 human body keypoints, including: nose, eyes, ears, shoulders, elbows, wrists, hips, knees, and ankles. The goal is to identify the positions of these keypoints by providing their normalized coordinates within each image. If a keypoint is not visible in the image, it is represented as [0.0, 0.0]. The keypoints are provided in the following order: [0] Nose, [1] Left eye, [2] Right eye, [3] Left ear, [4] Right ear, [5] Left shoulder, [6] Right shoulder, [7] Left elbow, [8] Right elbow, [9] Left wrist, [10] Right wrist, [11] Left hip, [12] Right hip, [13] Left knee, [14] Right knee, [15] Left ankle, [16] Right ankle. All keypoints are in [x, y] format, and the coordinates are normalized to be within [0, 1] based on the width and height of the image. Your output will be a sequence of 17 such [x, y] coordinates.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](000000393226.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: [[0.21,0.43], [0.0,0.0], [0.21,0.43], [0.0,0.0], [0.2,0.43], [0.2,0.46], [0.18,0.46], [0.21,0.5], [0.17,0.5], [0.22,0.53], [0.19,0.54], [0.19,0.56], [0.19,0.56], [0.17,0.62], [0.2,0.61], [0.16,0.68], [0.22,0.68]]
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1885
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Visual_Recognition
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'sequence_coords_similarity'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: hello, this is Source Description
