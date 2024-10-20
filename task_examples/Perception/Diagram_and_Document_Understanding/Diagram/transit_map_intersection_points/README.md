# Task: transit_map_intersection_points

## Task Description:

```
Given a query transit image, you are asked to answer 1. how many metro lines are included in the given map. 2. the name of intersection station(s) of two lines given by example question. The answer should be a list, containing one or multiple intersection stations' names.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](397.png)

```
Example Question: Line H and Line M
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'Number of lines': '5', 'Intersection station (s)': "['M2', 'M11']"}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2143
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Diagram
- **App**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Number of lines': 'exact_str_match', 'Intersection station (s)': 'jaccard_index_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Number of lines': 1, 'Intersection station (s)': 1}}
  - **Response Parse Function**: json
