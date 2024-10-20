# Task: topological_sort

## Task Description:

```
For a given Directed Acyclic Graph (DAG), your task is to output all possible topological orders. The output is a set of topological order.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](dag_example_3.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: [0->1->2->4->3,0->1->2->3->4]
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2844
- **Eval Context**: {}
- **Taxonomy Tree Path**: Mathematics;Graph_Theory
- **App**: Mathematics
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'answer': 'set_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
