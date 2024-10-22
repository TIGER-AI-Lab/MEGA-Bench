# Task: Knowledge graph understanding

## Task Description:

```
Given a knowledge graph from Game of Thrones, you will be provided with two characters. Your task is to determine their relationship based on the knowledge graph. Provide a list of all possible relationships. The possible relationships include "parent", "child", "sibling", "killed" and "partner". There could be multiple relationships between two characters. You need to output all relevant relationships in a list format, separated by commas. If the relationship isn't shown in the graph, answer "[unknown]".
```

![Image](GoT_kg.png)

## The 1-shot Example for Task Demonstration:

## Example Query:

```
Question: Petyr Baelish, Arya Stark
```

```
Demonstration example(s) of the task:
Example 1:
Example Question: Arya Stark, Sansa Stark
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: [sibling]
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3624
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Diagram;Diagram_QA
- **Application**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'set_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: The large knowledge graph image was collected from the Internet. Questions and answers were designed by the annotator
