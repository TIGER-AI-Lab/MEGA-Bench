# Task: counterfactual_arithmetic

## Task Description:

```
Perform calculations using the specified number system as required
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](Screenshot_2024-09-03_at_23.19.09.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 100
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5527
- **Eval Context**: {}
- **Taxonomy Tree Path**: Mathematics;Number_Theory
- **App**: Mathematics
- **Input Format**: Text-Based Images and Documents
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
