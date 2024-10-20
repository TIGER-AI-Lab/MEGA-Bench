# Task: orchestra_score_recognition

## Task Description:

```
This task involves analyzing a segment of a orchestra score to identify the specific piece and its composer. The input will be an image or a segment of sheet music, and the output should accurately identify the title of the orchestra and the (last) name of the composer.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0.jpg)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'Name': 'Symphony No. 5 in C Minor, Op. 67', 'Composer_last_name': 'Beethoven'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4030
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Music
- **App**: Knowledge
- **Input Format**: Text-Based Images and Documents
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Name': 'simple_str_match', 'Composer_last_name': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Name': 1, 'Composer_last_name': 1}}
  - **Response Parse Function**: json
