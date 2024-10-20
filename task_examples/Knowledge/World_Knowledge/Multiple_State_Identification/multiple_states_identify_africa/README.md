# Task: multiple_states_identify_africa

## Task Description:

```
Given a map with 5 countries randomly shaded in different colors, you need to output the country name that corresponds to each color: blue, orange, green, red, and purple.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Namibia,Liberia,Republic of the Congo,Republic of Cabo Verde,The Gambia
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4820
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Multiple_State_Identification
- **App**: Knowledge
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'sequence_accuracy_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
