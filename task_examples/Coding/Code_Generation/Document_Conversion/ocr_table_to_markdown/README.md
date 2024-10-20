# Task: ocr_table_to_markdown

## Task Description:

```
You are given an image of a table. You need to convert this to the simplest Markdown format, where we use exactly 3 hyphens to create the column header.
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
Answer: |Name|School|Gender|Weight|Height|
|--- |--- |--- |--- |--- |
|Kim|UCB|Male|52kg|168cm|
|Mariton|Stanford|Female|43kg|159cm|
|George|UCSB|Male|54kg|172cm|
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5967
- **Eval Context**: {}
- **Taxonomy Tree Path**: Coding;Code_Generation;Document_Conversion
- **App**: Coding
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'output': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'output': 1}}
  - **Response Parse Function**: answer_string
