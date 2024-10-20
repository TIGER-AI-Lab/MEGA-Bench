# Task: memorization_chinese_celebrity

## Task Description:

```
Please answer the name and nationality of the celebrity. For the name, please put last name in the front.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](kris_wu.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'name': 'Wu Yifan', 'nationality': 'Canadian'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 6433
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Memorization
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'name': 'multi_ref_phrase', 'nationality': 'multi_ref_phrase'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'name': 1, 'nationality': 1}}
  - **Response Parse Function**: json
