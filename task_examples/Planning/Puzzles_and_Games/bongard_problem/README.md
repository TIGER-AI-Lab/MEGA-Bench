# Task: bongard_problem

## Task Description:

```
The problem consists of two sets of images, typically six simple black and white diagrams in each set.
The left set of images follows one rule or pattern, while the right set follows a different rule.
Your task is to identify the patterns that distinguishes the two sets of images. The patterns should be selected from "entry shape", "entry size", "entry position", "entry color", "entry number", "entry orientation", "splicing feature". Sometimes multiple patterns are needed to distinguish the two sets, you should separate them by comma.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: entry size
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2299
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games
- **App**: Planning
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'set_precision'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
