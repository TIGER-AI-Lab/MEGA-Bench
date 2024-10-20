# Task: ocr_article_authors

## Task Description:

```
Please extract the first and last authors from the paper.
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
Answer: {'First Author': 'Alina Sturdza', 'Last Author': 'Richard Schwameis'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 6051
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Structured_Parsing
- **App**: Information_Extraction
- **Input Format**: Text-Based Images and Documents
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'First Author': 'simple_str_match', 'Last Author': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'First Author': 1, 'Last Author': 1}}
  - **Response Parse Function**: json
