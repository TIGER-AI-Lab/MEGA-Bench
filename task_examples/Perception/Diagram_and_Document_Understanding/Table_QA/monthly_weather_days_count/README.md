# Task: monthly_weather_days_count

## Task Description:

```
Given a screenshot of a weather webpage, count the number of days with different weather types in the current month: (1) sunny days (including partly cloudy and non-rainy/snowy days) (2) rainy days (3) snowy days
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](monthly_weather_days_count1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'sunny': '21', 'rainy': '10', 'snowy': '0'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3112
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Table_QA
- **App**: Perception
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'sunny': 'exact_str_match', 'rainy': 'exact_str_match', 'snowy': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'sunny': 1, 'rainy': 1, 'snowy': 1}}
  - **Response Parse Function**: json
