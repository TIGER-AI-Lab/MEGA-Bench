# Task: video_action_recognition

## Task Description:

```
Given the query video, you are asked to 1. answer the action category that the video describes. The answer should be selected from ('Eye Makeup', 'Draw eyebrows', 'Baby Crawling', 'Baby Crying','Playing Basketball', 'Playing Rugby', 'Bowling', 'Head Massage', 'Diving', 'Swimming', 'Haircut', 'Perm', 'Ice Dancing', 'Playing Guitar', 'Playing Ukulele', 'Playing Piano', 'Playing Electronic keyboard', 'SkateBoarding', 'Roller Skating', 'Typing'). 2. Whether the query video is plaied sequentially or reversely? The answer should be from ('sequential', 'reverse')
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: v_ApplyEyeMakeup_g01_c01.mp4]

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'Answer': "'Eye Makeup'", 'Order': "'sequential'"}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3879
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Temporal_Understanding
- **App**: Perception
- **Input Format**: Videos
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match', 'Order': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1, 'Order': 1}}
  - **Response Parse Function**: json
