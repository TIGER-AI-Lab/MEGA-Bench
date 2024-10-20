# Task: average_humidity_estimate_plot

## Task Description:

```
The plot shows the relative humidity at a place in the past 24 hours. Please estimate the average relative humidity from the plot. Provide the answer in a single positive real number between 0 and 1 without using any additional text, keep 2 significant digits.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](2_relative_huminidity_101_0.4885798611111112.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 0.49
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 219
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Diagram;Estimation
- **App**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'normalized_rmse'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
