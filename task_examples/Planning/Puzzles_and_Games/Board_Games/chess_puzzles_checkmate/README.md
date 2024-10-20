# Task: chess_puzzles_checkmate

## Task Description:

```
List all forced checkmate sequences with less than 30 plies. Do not include more moves if you are unsure: only the correct answers will be accepted. Moves that start from the black side shall start like this: "35... Rxa1+".
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0_iPz6e.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: ['23. Qc5+ Qb8 24. Rxd8#']
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5738
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games;Board_Games
- **App**: Planning
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'move_sequences': 'set_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'move_sequences': 1}}
  - **Response Parse Function**: answer_string
