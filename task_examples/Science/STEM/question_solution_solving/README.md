# Task: Question solution solving

## Task Description:

```
Given a screenshot from the Question Solutions website, solve the question and provide the correct answer following the per-example instruction.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](question_solution_solving1.png)

```
Example Question: Please make sure the result is numerical without unit
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1.43
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 562
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
