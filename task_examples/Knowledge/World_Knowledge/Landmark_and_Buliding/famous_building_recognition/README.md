# Task: Famous building recognition

## Task Description:

```
What is the name of the building in the picture and the year of its earliest construction completetion date or offcial opening date? Omit the "the" in your answer, and use the formal name of the building. For the construction completetion time, if you believe there is no certain answer recorded in the history, answer NA instead.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'name': 'Louvre Museum', 'year': '1793'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1769
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Landmark_and_Buliding
- **Application**: Knowledge
- **Input Format**: Photographs
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'name': 'exact_str_match_case_insensitive', 'year': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'name': 1, 'year': 1}}
  - **Response Parse Function**: json
- **Source Description**: Images and labels come from various websites. Questions were created by a human annotator.
