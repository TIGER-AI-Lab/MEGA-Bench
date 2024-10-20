# Task: video_to_camera_trajectory_retrieval

## Task Description:

```
Your task is to identify the correct camera trajectory of a 16-frame video. The first image displays five possible camera trajectories, labeled 1 to 5 from left to right. The remaining 16 images are 16 frames sampled from a video. Each frame of the video is split into left and right halves, both showing the same camera movement trajectory.

Based on the camera movement in the 16 frames, you need to determine which of the five trajectories in the first provided image matches the movement the best. Your answer should follow the format "Answer: $index$ ", where $index$ is the index of the matched trajectory, ranging from 1 to 5.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1-5.png)

![Image](video_1_frame_0000.png)

![Image](video_1_frame_0001.png)

![Image](video_1_frame_0002.png)

![Image](video_1_frame_0003.png)

![Image](video_1_frame_0004.png)

![Image](video_1_frame_0005.png)

![Image](video_1_frame_0006.png)

![Image](video_1_frame_0007.png)

![Image](video_1_frame_0008.png)

![Image](video_1_frame_0009.png)

![Image](video_1_frame_0010.png)

![Image](video_1_frame_0011.png)

![Image](video_1_frame_0012.png)

![Image](video_1_frame_0013.png)

![Image](video_1_frame_0014.png)

![Image](video_1_frame_0015.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 534
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Temporal_Understanding
- **App**: Perception
- **Input Format**: Videos
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
