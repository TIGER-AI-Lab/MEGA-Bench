# Task: table_understanding_fetaqa

## Task Description:



## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](F1.png)

```
Example Question: Who won the 1982 Illinois gubernatorial election, and how many votes was the margin?
Example Response: Answer: Thompson prevailed in the 1982 Illinois gubernatorial election by a 5,074 vote margin.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 989
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Table_QA
- **App**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
