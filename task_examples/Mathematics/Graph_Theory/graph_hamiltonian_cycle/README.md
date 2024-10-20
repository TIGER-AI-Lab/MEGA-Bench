# Task: graph_hamiltonian_cycle

## Task Description:

```
Given several images of graphs, the task is to determine how many of these graphs contain a Hamiltonian Cycle. Additionally, the specific graphs that include a Hamiltonian Cycle should be identified. This tests the AI's ability to find complex cyclic patterns.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](01.1.png)

![Image](01.2.png)

![Image](01.3.png)

![Image](01.4.png)

![Image](01.5.png)

![Image](01.6.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'Count': '4', 'Indices': '1,4,5,6'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 306
- **Eval Context**: {}
- **Taxonomy Tree Path**: Mathematics;Graph_Theory
- **App**: Mathematics
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Count': 'exact_str_match', 'Indices': 'set_precision'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Count': 1, 'Indices': 1}}
  - **Response Parse Function**: json