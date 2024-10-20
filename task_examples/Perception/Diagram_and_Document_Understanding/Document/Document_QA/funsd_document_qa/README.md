# Task: funsd_document_qa

## Task Description:

```
Answer the question based on the given screenshot of a scanned document.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: What is the field right next to ‘CAT- G- EXPENSES:’? You must answer the question using the text in the image directly.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: CAT-H-EXPENSES
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 504
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Document;Document_QA
- **App**: Perception
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
