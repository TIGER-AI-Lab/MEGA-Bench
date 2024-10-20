# Task: chart_vqa

## Task Description:

```
Please answer the question given a chart. Make sure the final answer is in the format of "Answer: ...", and ignore the unit if any.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](image_1.png)

```
Example Question: The water level in a port rises and falls on a certain day as shown in the diagram. How many hours on that day was the water level over $30 \mathrm{~cm}$? <image1>
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 13
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1138
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Diagram;Diagram_QA
- **App**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'answer': 'general_single_numerical_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
