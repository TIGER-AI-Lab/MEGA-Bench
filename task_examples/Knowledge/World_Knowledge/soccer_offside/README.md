# Task: soccer_offside

## Task Description:

```
The image depicts an offside moment during a soccer game. The key players are marked by colored numbers. Select the offside player from the given candidates.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1_process.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 3
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3937
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
