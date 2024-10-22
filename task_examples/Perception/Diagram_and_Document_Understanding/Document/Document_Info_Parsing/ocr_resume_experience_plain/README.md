# Task: Ocr resume experience plain

## Task Description:

```
Given a resume, you are suppposed to extract all the (working) experience of the person. You need to output like
ˋˋˋ
experience 1
experience 2
...
ˋˋˋ
You should omit the location and time, just put the name of the experience in each line.
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
Answer: PET SITTER\nCHILD CARE
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 6023
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Document;Document_Info_Parsing
- **Application**: Perception
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'output': 'str_set_equality_line_break'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'output': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: The resume screenshots were taken from various websites. Questions and answers were created by the annotator
