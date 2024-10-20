# Task: video_grounding_temporal

## Task Description:

```
Given a video and some sentences below, choose when the actions, or events or scenes described in the sentences start in the video. Specifically, imagine that we divide the video into several segments (segment1, segment2, segment3, ...) evenly and you need to choose the segment most related to the textual descriptions. Your output will be a positive integar, showing the correct segment.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 1.mp4]

```
Example Question: Suppose the video is divided into 10 segments, every sgement is 4 seconds. When did a black dog first appear? 
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 6
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2390
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Temporal_Understanding
- **App**: Perception
- **Input Format**: Videos
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
