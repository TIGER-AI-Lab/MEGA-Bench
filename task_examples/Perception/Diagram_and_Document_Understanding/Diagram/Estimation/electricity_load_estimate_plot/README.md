# Task: Electricity load estimate plot

## Task Description:

```
The plot shows the load data from electricity transformers recorded. Please estimate the load for the next time interval from the plot. Provide the answer as a positive real number without including any additional text. And here is the meaning for different plot:
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

![Image](HUFL_0.4732.png)

```
Example Question: HUFL
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 0.4732
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1984
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Diagram;Estimation
- **Application**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'normalized_rmse'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: The temporal data were collected from Informer and AutoFormer. The annotator re-processed the data to design a more specific task
