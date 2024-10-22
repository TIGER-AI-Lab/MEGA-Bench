# Task: Ocr resume school plain

## Task Description:

```
Please extract the education information from a resume. You need to output the like
 ˋˋˋ
School 1
School 2
School 3
ˋˋˋ 
If the person obtains multiple degress from the same university, you need to output it multiple times. The locations should be omitted.
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
Answer: MEGGIETON HIGH SCHOOL
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 6093
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Structured_Parsing
- **Application**: Information_Extraction
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'output': 'str_set_equality_line_break'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'output': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Resumes taken from various personal websites. Questions and answers were created by the annotator.
