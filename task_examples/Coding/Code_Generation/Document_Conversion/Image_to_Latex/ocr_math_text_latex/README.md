# Task: Ocr math text latex

## Task Description:

```
Can you translate a screenshot into its latex source. Ignore the citations like [2,3]. For all the math symbols, use $...$. Ignore all the formatting like \mathbf, \emph, \bold, \text, \mid, \left, etc. If there are both superscript and subscript, always write subscript first.
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
Answer: Another line of works propose to modify the diffusion trajectory through the integration of cross-modality information. Specifically, the cross-modal information, denoted as $r_\phi(y, x_0)$, is extracted from any conditional input $y$ and original sample $x_0$ with relational network $r_{\phi}(\cdot)$. And then it can be injected into the forward process as an additional bias to adapt the diffusion trajectory:
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 6037
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Coding;Code_Generation;Document_Conversion;Image_to_Latex
- **Application**: Coding
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'output': 'text_with_latex_expr_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'output': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data are collected from website, and the question and answer are designed by human annotator to match text with \LaTeX
