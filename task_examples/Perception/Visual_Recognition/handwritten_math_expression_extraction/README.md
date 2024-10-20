# Task: handwritten_math_expression_extraction

## Task Description:

```
Please write out the expression of the formula in the image using LaTeX format. Avoid unnecessary brackets in your output. Do NOT surround the answer with "$...$".
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
Answer: ( 2 ) 2 N a O H + C u S O _4 = N a _2 S O _ 4 + C u ( O H )_2 \downarrow
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1843
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Visual_Recognition
- **App**: Perception
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'latex_expr_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
