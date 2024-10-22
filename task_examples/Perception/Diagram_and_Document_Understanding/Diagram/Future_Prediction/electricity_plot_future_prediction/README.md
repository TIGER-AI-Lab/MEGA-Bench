# Task: Electricity plot future prediction

## Task Description:

```
You are provided with a plot showing the electricity consumption of a household in the past 77 hours. The x-axis indicates time and the y-axis indicates electricity consumption amount. Your task is to predict the electricity consumption of the household in the next hour using a single real number without any additional text.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0_0.005339028296849973.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 0.00533
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 425
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Diagram;Future_Prediction
- **Application**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'normalized_rmse'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: The temporal data were collected from AutoFormer. The annotator re-processed the data to design a more specific task
