# Task: medical_cell_recognition

## Task Description:

```
Given the microscopy image, please identify which cell tissue that the hightlight area of the query image belongs to? The answer should be selected from (cytoplasm, cell nucleus, erythrocytes, platelet, red blood cell, white blood cell, cytosol).
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](130.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: platelet
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4481
- **Eval Context**: {}
- **Taxonomy Tree Path**: Science;Life_Sciences;Medical
- **App**: Science
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
