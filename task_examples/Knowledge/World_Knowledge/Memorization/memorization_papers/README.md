# Task: memorization_papers

## Task Description:

```
Please read a figure or diagram to answer the name of the famous paper and the name of the first author as it appears on the paper.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](F2.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'paper': 'Generative Adversarial Nets', 'author': 'Ian J. Goodfellow'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 6447
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Memorization
- **App**: Knowledge
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'paper': 'simple_str_match', 'author': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'paper': 1, 'author': 1}}
  - **Response Parse Function**: json
