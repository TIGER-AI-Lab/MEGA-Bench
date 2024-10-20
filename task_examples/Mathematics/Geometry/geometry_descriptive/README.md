# Task: geometry_descriptive

## Task Description:

```
Please answer the geometry-related question given a diagram. Make sure the final answer is in the format of "Answer: ...", and ignore the unit if any.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](image_1.png)

```
Example Question: Seven sticks lay on top of each other. Stick 2 lays right at the bottom. Stick 6 lays right on top. Which stick lays exactly in the middle? <image1>
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 3
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 911
- **Eval Context**: {}
- **Taxonomy Tree Path**: Mathematics;Geometry
- **App**: Mathematics
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'general_single_numerical_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
