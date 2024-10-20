# Task: cam_traj_to_video_selection

## Task Description:

```
This task requires you to understand the camera movement of a video. In each question, the first image shows a camera movement trajectory, then two videos with different camera movement trajectories are presented. You need to determine which of these two videos accurately matches the reference camera trajectory in the first image. The output should be 'left' if the first video is the correct match, 'right' if the second video is the correct match.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](image_1.png)

[Please watch the local video: left_video_1.mp4]

[Please watch the local video: left_video_2.mp4]

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: left
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 777
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Temporal_Understanding
- **App**: Perception
- **Input Format**: Videos
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
