# Task: Ad_count_detection

## Task Description:

```
Given a screenshot of a webpage containing posters and ads, count the total number of distinct advertisements present on the page.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](Ad_count_detection1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2070
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Counting
- **App**: Perception
- **Input Format**: User Interface Screenshots
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match', 'reason': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1, 'reason': 1}}
  - **Response Parse Function**: answer_string
