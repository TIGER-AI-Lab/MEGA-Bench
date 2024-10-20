# Task: perception_test_video_action_count

## Task Description:

```
Your task is to determine the number of actions requested in the corresponding question based on the given video.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 0.mp4]

```
Example Question: How many times did the person launch objects on the table?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 3
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1323
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Temporal_Understanding
- **App**: Perception
- **Input Format**: Videos
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
