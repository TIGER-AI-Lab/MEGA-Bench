# Task: ili_ratio_future_prediction

## Task Description:

```
The plot shows the historical weekly weighted ILI (Influenza-Like Illness) ratios in the United States. The x-axis represents the date, and the y-axis represents the percentage of weighted ILI. Please predict the weighted ILI ratio for the next week based on the observed trends in the plot. Provide the answer as a positive real number without including any additional text.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0_ILI_2.4871.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 2.4871
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1941
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Diagram;Future_Prediction
- **App**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'normalized_rmse'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
