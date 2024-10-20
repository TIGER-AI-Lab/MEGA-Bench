# Task: science_molecule_chemistry

## Task Description:

```
You are given a multiple-choice chemistry question.
YOUR TASK is to read the question and select the correct answer from the provided options.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](chemistry_1.png)

```
Example Question: Which solution has a higher concentration of green particles?

the left solution
neither; their concentrations are the same
the right solution
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: neither; their concentrations are the same
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 939
- **Eval Context**: {}
- **Taxonomy Tree Path**: Science;Chemistry
- **App**: Science
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
