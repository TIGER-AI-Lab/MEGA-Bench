# Task: Ishihara test

## Task Description:

```
Identify what a person with normal vision or protan, deutan, and tritan colour blindness would see, even if faintly.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'protanopia': '["5"]', 'deuteranopia': '[""]', 'tritanopia': '["5"]', 'normal_vision': '["5"]'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3206
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;Human_and_Culture
- **Application**: Knowledge
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'protanopia': 'set_precision', 'deuteranopia': 'set_precision', 'tritanopia': 'set_precision', 'normal_vision': 'set_precision'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'protanopia': 2, 'deuteranopia': 1, 'tritanopia': 1, 'normal_vision': 1}}
  - **Response Parse Function**: json
- **Source Description**: Images come from various websites. Questions and annotations were created by a human annotator.
