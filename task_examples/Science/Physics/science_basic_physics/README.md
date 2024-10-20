# Task: science_basic_physics

## Task Description:

```
You are given a multiple-choice physics question.
YOUR TASK is to read the question and select the correct answer from the provided options.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](phy_1.png)

```
Example Question: During this time, thermal energy was transferred from () to (). Select from below

the surroundings . . . each salmon
each salmon . . . the surroundings
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: the surroundings . . . each salmon
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1579
- **Eval Context**: {}
- **Taxonomy Tree Path**: Science;Physics
- **App**: Science
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
