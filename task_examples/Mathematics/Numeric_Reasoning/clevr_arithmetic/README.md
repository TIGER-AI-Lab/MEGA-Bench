# Task: Clevr arithmetic

## Task Description:

```
Answer an arithmetic question based on image(s) consisting of multiple objects. Answer should be an integer.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: Add 3 big gray rubber cubes. How many big gray rubber cubes are in the image?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 4
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1253
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Mathematics;Numeric_Reasoning
- **Application**: Mathematics
- **Input Format**: Photographs
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from Clevr
