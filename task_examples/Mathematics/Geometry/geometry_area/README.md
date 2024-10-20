# Task: geometry_area

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
Example Question: In the picture $A B C D$ is a rectangle with $A B=16, B C=12$. Let $E$ be such a point that $A C \perp C E, C E=15$. If $F$ is the point of intersection of segments $A E$ and $C D$, then the area of the triangle $A C F$ is equal to
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 75
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1899
- **Eval Context**: {}
- **Taxonomy Tree Path**: Mathematics;Geometry
- **App**: Mathematics
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
