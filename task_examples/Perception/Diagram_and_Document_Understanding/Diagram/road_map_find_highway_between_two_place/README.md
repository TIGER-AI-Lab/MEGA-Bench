# Task: road_map_find_highway_between_two_place

## Task Description:

```
Given the query road map and two locations in the image, you are asked to answer the name of the highway that most likely connects these two locations.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](web-1.png)

```
Example Question: Locations: Pickering and Oshawa. Answer should be highway code
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 2
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4631
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Diagram
- **App**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'highway': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'highway': 1}}
  - **Response Parse Function**: answer_string
