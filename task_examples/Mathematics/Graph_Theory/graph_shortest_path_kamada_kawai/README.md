# Task: graph_shortest_path_kamada_kawai

## Task Description:

```
Find the shortest path length between two marked nodes in a graph. This evaluates the AI's ability to optimize routes in complex networks
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](01.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 4
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1110
- **Eval Context**: {}
- **Taxonomy Tree Path**: Mathematics;Graph_Theory
- **App**: Mathematics
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Length': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Length': 1}}
  - **Response Parse Function**: answer_string
