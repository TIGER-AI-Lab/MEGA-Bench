# Task: Ocr math equation

## Task Description:

```
Given an image containing a block math equation, you need to parse to its shortest latex form. Please omit $ sign and ignore the formating command like \mathbf, \bold, \text, \mid, \left, etc.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](Figure1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: q(\x_1, \ldots, x_T | x_0) = \prod_{t=1}^{T} q({x_t | x_{t-1}).
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 6079
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Coding;Code_Generation;Document_Conversion;Image_to_Latex
- **Application**: Coding
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'output': 'latex_expr_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'output': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data are collected from website, and the question and answer are designed by human annotator to match \LaTeX
