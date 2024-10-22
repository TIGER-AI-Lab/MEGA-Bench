# Task: Symbolic graphics programs computer aided design

## Task Description:

```
Given a symbolic graphics program, the task is to answer a related question by understanding the program.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: How many visible cylindrical sections does the CAD object have?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Two
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4918
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Coding;Code_Understanding;Symbolic_Graphics_Programming
- **Application**: Coding
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'multi_ref_phrase'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data and answer are collected from SGP-Bench
