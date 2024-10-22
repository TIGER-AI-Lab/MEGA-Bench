# Task: Traffic future prediction from line plot

## Task Description:

```
You are provided with a plot of hourly data showing the road occupancy rates measured by a sensor on San Francisco Bay area freeways in the past 96 hours. The x-axis indicates time and the y-axis indicates the road occupancy rate. Your task is to predict the road occupancy rate in the next hour using a single real number without any additional text.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](traffic_0_0.0148.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 0.0148
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 84
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
