# Task: chess_puzzles_crushing

## Task Description:

```
Generate a chess tactics puzzle solution from the following position. Assume the opponent always plays the best move. Playing moves other than the ones in the puzzle solution should either result in being in a losing or drawing position. Solutions will have less than 10 plies. Moves that start from the black side shall start like this: \"35... Rxa1+\".
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0_DRqZD.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 12... Bxc2+ 13. Kxc2 Rxe1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5724
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games;Board_Games
- **App**: Planning
- **Input Format**: User Interface Screenshots
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'puzzle_solution': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'puzzle_solution': 1}}
  - **Response Parse Function**: answer_string
