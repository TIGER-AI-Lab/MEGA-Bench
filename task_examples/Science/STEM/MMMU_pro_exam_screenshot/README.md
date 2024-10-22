# Task: Mmmu pro exam screenshot

## Task Description:

```
Answer the multiple choice question in the image. The question comes from college-level exams, which tests your domain-specific knowledge and reasoning ability.Your response should be of the following format: 'Answer: $LETTER' (without quotes) where LETTER is one of the options. Think step by step before answering but only output the answer.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](validation_Math_29.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: D
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4087
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Science;STEM
- **Application**: Science
- **Input Format**: User Interface Screenshots
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from MMMU-Pro, and the questions and answers are adapted to match strings
