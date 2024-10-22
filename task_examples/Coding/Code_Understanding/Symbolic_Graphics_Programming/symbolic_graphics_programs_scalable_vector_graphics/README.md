# Task: Symbolic graphics programs scalable vector graphics

## Task Description:

```
Given a symbolic graphics program, the task is to answer a related question.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](color_173.png)

```
Example Question: What color is the nose of the object? Answer the color name.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: pink
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4932
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
