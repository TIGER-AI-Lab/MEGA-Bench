# Task: electricity_future_prediction_from_table

## Task Description:

```
The 6 tables shows the hourly electricity of a household in the past 3 days. Please predict the hourly electricity consumption of the household in the following day at a given hour. Provide the answer using a single real number without any additional text.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](table_0_time_23_00_0.037.png)

```
Example Question: What's the electricity consumption at 23:00 on the fourth day?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 0.037
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1594
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Table_QA
- **App**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'normalized_rmse'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
