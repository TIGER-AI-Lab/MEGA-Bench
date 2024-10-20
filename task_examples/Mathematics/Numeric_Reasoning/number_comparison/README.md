# Task: number_comparison

## Task Description:

```
Answer the question with the numerical number.
```

![Image](Picture1.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
Example Question: Can you answer Q1?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 10.8
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3748
- **Eval Context**: {}
- **Taxonomy Tree Path**: Mathematics;Numeric_Reasoning
- **App**: Mathematics
- **Input Format**: Text-Based Images and Documents
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
