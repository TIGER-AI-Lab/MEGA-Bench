# Task: rebus

## Task Description:

```
Return the phrase that the rebus is referring to. Do not include numeric digits in your answer. Use American spelling.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: forget it
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3168
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games
- **App**: Planning
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'phrase': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'phrase': 1}}
  - **Response Parse Function**: answer_string
