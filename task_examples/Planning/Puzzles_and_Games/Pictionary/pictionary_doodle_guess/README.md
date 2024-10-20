# Task: pictionary_doodle_guess

## Task Description:

```
A collection of doodles from real humans and a few characters from the final answer are provided (with the remaining characters masked using '*'). The task is to guess what the final answer is based on these doodles.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](The_Eiffel_Tower.png)

```
Example Question: The final answer is: T** Ei**** T****
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: The Eiffel Tower
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 6319
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games;Pictionary
- **App**: Planning
- **Input Format**: Artistic and Creative Content
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
