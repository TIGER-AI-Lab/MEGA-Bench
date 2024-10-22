# Task: Relative reflectance of different regions

## Task Description:

```
Given the query image with three circled region (A, B, C). Please sort the circled regions by brightness from light to dark。The answer should be a list including the letter. Beside, the order matters.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](test_Relative_Reflectance_1_1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: ['C', 'A', 'B']
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3988
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Physical_Understanding;Lighting_and_Shading
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'sequence_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images come from BLINK, the annotator added one more point per image and converted the task into a reflectance sorting task
