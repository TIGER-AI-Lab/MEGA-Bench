# Task: multi_load_type_prediction_from_plot

## Task Description:

```
The plot shows load data from electricity transformers recorded every 15 minutes in 2016. Please classify which load type (HUFL, HULL, MUFL, MULL, LUFL, LULL) each plot corresponds to, and provide your answer by listing the correct load types in the order that the images appear, without including any additional text.

HUFL: High UseFul Load
HULL: High UseLess Load
MUFL: Middle UseFul Load
MULL: Middle UseLess Load
LUFL: Low UseFul Load
LULL: Low UseLess Load
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0_HUFL.png)

![Image](0_HULL.png)

![Image](0_LUFL.png)

![Image](0_LULL.png)

![Image](0_MUFL.png)

![Image](0_MULL.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: HUFL, HULL, LUFL, LULL, MUFL, MULL
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 117
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Diagram;Future_Prediction
- **App**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'sequence_accuracy_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
