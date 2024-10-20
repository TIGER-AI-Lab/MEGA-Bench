# Task: ocr_resume_employer_plain

## Task Description:

```
YOu are supposed to extract all the employers of the person from its CV. You need to output like
ˋˋˋ
Employer 1
Employer 2
...
ˋˋˋ
You just need to output the employer name without time or location, etc.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](Figure1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Digital Agency One\nCapital Agency Two\nAd Agency Number Three
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5995
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Document;Document_Info_Parsing
- **App**: Perception
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'output': 'str_set_equality_line_break'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'output': 1}}
  - **Response Parse Function**: answer_string
