# Task: math_exams_v

## Task Description:

```
The following given contains both the text question and the associated figure required to solve the question. Your task is to answer the question in the image. For multiple-choice questions, only answer the choice letter with "Answer: $CHOICE_LETTER " .
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](image_1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: D
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1210
- **Eval Context**: {}
- **Taxonomy Tree Path**: Mathematics;General
- **App**: Mathematics
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'answer': 'general_single_numerical_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
