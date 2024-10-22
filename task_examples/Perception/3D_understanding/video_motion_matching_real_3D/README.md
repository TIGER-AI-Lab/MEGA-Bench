# Task: Video motion matching real 3d

## Task Description:

```
Given a real-world video and several reconstructed videos, the task is to identify the reconstructed video that corresponds to the action performed in the real-world video.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 1_1.mp4]

[Please watch the local video: 2_2.mp4]

[Please watch the local video: 3_2.mp4]

[Please watch the local video: 1_2.mp4]

[Please watch the local video: 4_2.mp4]

```
Example Question: The first video is a real-world video, and the subsequent videos (1, 2, 3, 4) are reconstructed videos. which is the corresponding reconstructed video?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 3
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 6376
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;3D_understanding
- **Application**: Perception
- **Input Format**: Videos
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Videos were collected from the project page of ~\citet{shen2024world-grounded-human-motion}. Questions and answers were created by the annotator
