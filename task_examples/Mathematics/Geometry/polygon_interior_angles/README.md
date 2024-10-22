# Task: Polygon interior angles

## Task Description:

```
List all of the interior angles of the polygon in order, starting from the left-most point and going clockwise. Angles must be listed in degrees, rounded to two decimal places. Due to rounding, the sum of the interior angles may not be an integer and that's okay. Do not include the degree symbol. If there are overlapping edges, then go to the next point that would be clockwise in the current segment. Resize the image to the original resolution before estimating the angles.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0.png)

```
Example Question: Original resolution: 307x269
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 26.67,60.49,92.83
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 2098
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Mathematics;Geometry
- **Application**: Mathematics
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'interior_angles': 'angle_seq_float_rmse'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'interior_angles': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from screenshots by human annotator
