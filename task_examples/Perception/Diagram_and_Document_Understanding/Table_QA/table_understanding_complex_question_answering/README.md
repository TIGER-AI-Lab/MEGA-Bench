# Task: Table understanding complex question answering

## Task Description:



## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](f1.png)

```
Example Question: what is france and germany's deficit combined?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 69.9
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4950
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Table_QA
- **Application**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Tables were collected from WikiTableQuestions and TabFact. Questions and answers were designed by the annotator
