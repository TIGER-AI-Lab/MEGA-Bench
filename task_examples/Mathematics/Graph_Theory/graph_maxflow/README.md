# Task: Graph maxflow

## Task Description:

```
You are given a weighted directed graph and two query nodes. (one source node in red and one sink node in blue). The source node is the
node where the flow starts and the sink node is the node where the flow ends.
YOUR TASK is to solve the maxflow problem given the weighted directed graph. Definition of Maxflow problem:
In the max flow problem, we have a directed graph with a source node s and a sink node t, and each edge has a capacity (integer
valued, colored in green) that represents the maximum amount of flow that can be sent through it.
The goal is to find the maximum amount of flow that can be sent from s to t, while respecting the capacity constraints on the
edges.
Please compute the maximum flow from the red source node to the blue sink node.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](maxflow_1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 11
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 334
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Mathematics;Graph_Theory
- **Application**: Mathematics
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from IsoBench, and the questions and answers are adapted by human annotator
