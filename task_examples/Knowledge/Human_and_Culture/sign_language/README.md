# Task: sign_language

## Task Description:

```
Given a video of American Sign Language, your task is to recognize its meaning. The answer is typically one or a few words.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: AGAIN_repeat.mp4]

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: again
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3098
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;Human_and_Culture
- **App**: Knowledge
- **Input Format**: Videos
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'multi_ref_phrase'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
