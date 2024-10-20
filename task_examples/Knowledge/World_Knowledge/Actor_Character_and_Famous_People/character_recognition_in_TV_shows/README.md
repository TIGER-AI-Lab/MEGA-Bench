# Task: character_recognition_in_TV_shows

## Task Description:

```
Given a screenshot from a TV show website, identify the **full names** of the characters (not the actors). If the screenshot has more than one character, list their names from left to right, separated by commas.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](character_recognition_in_TV_shows1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Flynne Fisher
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4439
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Actor_Character_and_Famous_People
- **App**: Knowledge
- **Input Format**: User Interface Screenshots
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'name': 'set_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'name': 1}}
  - **Response Parse Function**: answer_string
