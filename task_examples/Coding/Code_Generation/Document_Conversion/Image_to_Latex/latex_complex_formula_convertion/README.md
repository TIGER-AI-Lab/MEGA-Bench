# Task: Latex complex formula convertion

## Task Description:

```
Given a math formula in the image, please convert it into LaTeX code. Note: use '\text' instead of '\mbox', use \quad' instead of '\ \ \ \', use '\frac' instead of '\over', use '\begin{pmatrix}' instead of '\left(\begin{array}{cc}' and '\end{array} \right)', use ' ' instead of '\ '
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: \begin{align*}-\div (y^{1-2m}\nabla w)=0\text{in}\\mathbb R^n\times\mathbb R_+;w\big|_{y=0}=|u|\end{align*}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 2126
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Coding;Code_Generation;Document_Conversion;Image_to_Latex
- **Application**: Coding
- **Input Format**: Text-Based Images and Documents
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'latex_expr_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data are collected from [latex-formulas](https://huggingface.co/datasets/OleehyO/latex-formulas) and [TexTeller](https://github.com/OleehyO/TexTeller?tab=readme-ov-file), and the question and answer are designed by human annotator
