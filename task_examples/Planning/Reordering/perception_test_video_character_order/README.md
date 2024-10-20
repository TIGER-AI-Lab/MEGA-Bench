# Task: perception_test_video_character_order

## Task Description:

```
The task involves identifying the order of letters as a person writes, types, or arranges them, predicting subsequent letters, and reversing letter sequences in various scenarios. Answer the question absed on the video. Do not output any punctuation.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 0.mp4]

```
Example Question: What letter did the person write first on the paper?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: l
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 444
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Reordering
- **App**: Planning
- **Input Format**: Videos
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
