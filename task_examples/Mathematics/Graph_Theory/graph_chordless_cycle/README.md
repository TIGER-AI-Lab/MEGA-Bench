# Task: graph_chordless_cycle

## Task Description:

```
Find the size of the largest chordless cycle (a cycle with no shortcuts) in a graph. This evaluates the AI's ability to identify specific substructures within complex graphs.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](01.png)

```
Example Question: What's the size of the largest chordless cycle (a cycle with no shortcuts) in the graph?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 6
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 103
- **Eval Context**: {}
- **Taxonomy Tree Path**: Mathematics;Graph_Theory
- **App**: Mathematics
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
