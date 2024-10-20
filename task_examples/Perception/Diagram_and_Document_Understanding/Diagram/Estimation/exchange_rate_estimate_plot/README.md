# Task: exchange_rate_estimate_plot

## Task Description:

```
The plot shows the daily exchange rates (based on US dollars) of eight different countries in 1990. Please estimate the exchange rate for the next day from the plot. All numbers are normalized to be within [0.0, 1.0], so simple memorization based on historical data cannot work. Provide the answer as a positive real number without including any additional text.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](exchange_rate_0_0.3836.png)

```
Example Question: Australia
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 0.3836
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 26
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Diagram;Estimation
- **App**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'normalized_rmse'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
