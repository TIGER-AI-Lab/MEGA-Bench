# Task: geometry_solid

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
Example Question: <image1> In the picture above we see a cube in two different positions. The six sides of the cube look like this: <image2> Which side is opposite to <image3>? <image4>
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: C
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1857
- **Eval Context**: {}
- **Taxonomy Tree Path**: Mathematics;Geometry
- **App**: Mathematics
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'general_single_numerical_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
