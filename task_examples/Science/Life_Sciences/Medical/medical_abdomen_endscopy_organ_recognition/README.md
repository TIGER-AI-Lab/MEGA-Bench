# Task: medical_abdomen_endscopy_organ_recognition

## Task Description:

```
Given the endscropy medical images in the Abdomen, please recognize which organs can appropriately describe the marked areas in the given query images. The answer should be a list including the organ types that represent the query images in order. The answer should be selected from (cecum, fascia covered kidney parenchyma, fascia uncovered kidney, parenchyma, gallbladder, kidney boundary, liver, pylorus, small intestine, z line)
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1049.png)

![Image](1060.png)

![Image](1072.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: liver, gallbladder, fascia uncovered kidney parenchyma
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2243
- **Eval Context**: {}
- **Taxonomy Tree Path**: Science;Life_Sciences;Medical
- **App**: Science
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'sequence_accuracy_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
