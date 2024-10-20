# Task: stock_price_future_prediction

## Task Description:

```
The plot shows the normalized historical closing prices of 15 different companies' stocks from 2020 to 2023. Please predict the normalized closing price for the next day based on the stock price trends. Provide the answer as a positive real number with exactly 4 significant digits without including any additional text.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0_AAPL_0.5453.png)

```
Example Question: Apple
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 0.5453
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2056
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Diagram;Future_Prediction
- **App**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'normalized_rmse'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
