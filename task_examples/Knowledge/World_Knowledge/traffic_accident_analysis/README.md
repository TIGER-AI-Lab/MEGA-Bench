# Task: traffic_accident_analysis

## Task Description:

```
Given an image of a traffic accident, you need to explain why Vehicle A should be held responsible.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Response: Answer: 追撞前车尾部的，均为A车全责。
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 102
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge
- **App**: Knowledge
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'explanation': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'explanation': 1}}
  - **Response Parse Function**: answer_string
