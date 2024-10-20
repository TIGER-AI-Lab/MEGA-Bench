# Task: sta_action_localization_video

## Task Description:

```
The task involves identifying when specific actions occur within a video. The actions may happen at the beginning, middle, end, or entire video. The answer should use one of word above to specify the timing of the action within the sequence.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 0.mp4]

```
Example Question: In the given video, when does the action 'person fixes their hair' take place?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: entire
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 379
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Temporal_Understanding
- **App**: Perception
- **Input Format**: Videos
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
