# Task: logical_reasoning_fit_pattern

## Task Description:

```
Given the query image including sequence of images and question mark, and suggested image choices, you are asked to identify the pattern and work out which one of the suggested images would fit this pattern to complete the sequence. The answer would replace the question mark.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](v1_26.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: B
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4411
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games
- **App**: Planning
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
