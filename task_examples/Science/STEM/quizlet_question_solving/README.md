# Task: Quizlet question solving

## Task Description:

```
Given a screenshot from the Quizlet website, solve the question and provide the correct answer. If the question is a multiple-choice question, you should only output the option following the format of "Answer: $choice-letter-1$, $choice-letter-2$, ...".
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](quizlet_question_solving1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 0.625
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 2026
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Science;STEM
- **Application**: Science
- **Input Format**: User Interface Screenshots
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'general_single_numerical_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from webpage screenshots by human annotator
