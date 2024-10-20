# Task: video_camera_motion_description

## Task Description:

```
Only watch the first five seconds of the following video and then please describe the primary and main movement of the camera in the video below. Your answer should be selected from the following options: {'steady','moving up','moving down','turning left','turning right','shaking','zooming in','zooming out','rotating clockwise', 'rotating counterclockwise'}.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 1.mp4]

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: shaking
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2271
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Temporal_Understanding
- **App**: Perception
- **Input Format**: Videos
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
