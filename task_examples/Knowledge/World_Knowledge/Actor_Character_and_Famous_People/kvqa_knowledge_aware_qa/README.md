# Task: kvqa_knowledge_aware_qa

## Task Description:

```
Answer a query about the bio of a famous person in the given image.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: For how many years did the person in the image live?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 71
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1425
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Actor_Character_and_Famous_People
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
