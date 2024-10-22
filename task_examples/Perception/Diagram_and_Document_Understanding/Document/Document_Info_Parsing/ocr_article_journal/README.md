# Task: Ocr article journal

## Task Description:

```
Please extract the DOI of the paper.
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
Answer: 10.1007/s00066-017-1178-x
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 6009
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Document;Document_Info_Parsing
- **Application**: Perception
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'doi': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'doi': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: The article screenshots were taken from various websites. Questions and answers were created by the annotator
