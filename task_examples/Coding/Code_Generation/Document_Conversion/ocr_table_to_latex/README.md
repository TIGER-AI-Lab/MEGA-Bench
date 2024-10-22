# Task: Ocr table to latex

## Task Description:

```
Given a table in an image, you are supposed to convert that to the simplest latex code following:
ˋˋˋ
\begin{tabular}[...]
....
\end{tabular}
ˋˋˋ
Please do not use any style command like \textbf, etc. We need to use \hline for all the horizontal lines.
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
Answer: \begin{tabular}{|l|l|l|l|l|}
\hline
Name    & School   & Gender & Weight & Height \\ \hline
Kim     & UCB      & Male   & 52kg   & 168cm  \\ \hline
Mariton & Stanford & Female & 43kg   & 159cm  \\ \hline
George  & UCSB     & Male   & 54kg   & 172cm  \\ \hline
\end{tabular}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5981
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Coding;Code_Generation;Document_Conversion
- **Application**: Coding
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'output': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'output': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data are collected from website, and the question and answer are designed by human annotator
