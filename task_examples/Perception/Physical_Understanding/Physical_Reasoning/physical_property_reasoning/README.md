# Task: physical_property_reasoning

## Task Description:

```
Tell the physical property of the object in an image
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0.png)

```
Example Question: What properties does this substance lack? Conductivity or ductility or lower density than water.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: lower density than water
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 734
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Physical_Understanding;Physical_Reasoning
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
