# Task: mindmap_elements_parsing

## Task Description:

```
According to the query mind map, please find out the elements that belong to the given parent note (category) in the example question. The answer should be a list, containing one or multiple elements.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](274.png)

```
Example Question: stick to the edges of the supermarket
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: ['frozen produce', 'fresh produce']
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2462
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Diagram;Diagram_QA
- **App**: Perception
- **Input Format**: Artistic and Creative Content
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'elements': 'set_equality_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'elements': 1}}
  - **Response Parse Function**: answer_string
