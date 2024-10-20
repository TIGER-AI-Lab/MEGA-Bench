# Task: code_error_line_identification

## Task Description:

```
Given a piece of program code, identify the most obvious error. Output the line number on the left where the error occurs. Attention: Do not invoke any external compilers or related programs.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](01.png)

```
Example Question: Where the error occurs?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 16
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1655
- **Eval Context**: {}
- **Taxonomy Tree Path**: Coding;Code_Debugging
- **App**: Coding
- **Input Format**: Text-Based Images and Documents
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Line': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Line': 1}}
  - **Response Parse Function**: answer_string
