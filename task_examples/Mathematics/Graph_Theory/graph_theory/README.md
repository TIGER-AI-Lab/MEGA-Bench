# Task: graph_theory

## Task Description:

```
Please answer the graph-related question given a query image and the question description. Make sure the final answer is in the format of "Answer: ...", and ignore the unit if any.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](image_1.png)

```
Example Question: Which point in the labyrinth can we get to, starting at point $O$? <image1>
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: C
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 576
- **Eval Context**: {}
- **Taxonomy Tree Path**: Mathematics;Graph_Theory
- **App**: Mathematics
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
