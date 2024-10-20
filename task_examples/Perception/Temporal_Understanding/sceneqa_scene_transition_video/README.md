# Task: sceneqa_scene_transition_video

## Task Description:

```
This task involves analyzing videos to describe how scenes transition, identifying the changes in location or context throughout the video. The goal is to output a description that matches the scene changes accurately, providing the correct sequence of transitions as seen in the video. If specific place names can be identified, include those names in the description.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 1.mp4]

```
Example Question: What are the scene transitions in the video?
Example Response: Answer: From Scarlett's house to New Orleans.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 753
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Temporal_Understanding
- **App**: Perception
- **Input Format**: Videos
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
