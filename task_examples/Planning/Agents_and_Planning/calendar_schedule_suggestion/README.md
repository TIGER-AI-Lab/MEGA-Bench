# Task: Calendar schedule suggestion

## Task Description:

```
Given a Google Calendar with existing occupied time slots, you should identify all possible starting times for a meeting within a specified time range and duration. The available starting times should be based on 15-minute intervals (e.g., :00, :15, :30, :45). The input has three parts: the target meeting's possible time range, duration, and date (Monday to Friday). If there is no suitable time, answer with an empty set: [].
```

![Image](Screenshot_2024-08-25_at_10.21.39_PM.png)

## The 1-shot Example for Task Demonstration:

## Example Query:

```
Question: 2:00pm to 6:00pm, Monday, 1hr
```

```
Demonstration example(s) of the task:
Example 1:
Example Question: 9:00am to 10:30am, Monday, 30min
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: [10:00am]
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 2332
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning
- **Application**: Planning
- **Input Format**: User Interface Screenshots
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'starting time': 'set_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'starting time': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from Google Calendar by human annotator, and the questions and answers are designed by human annotator to identify all possible starting times for a meeting within a specified time range and duration
