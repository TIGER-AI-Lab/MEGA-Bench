# Task: Chess sygyzy endgames

## Task Description:

```
Given the following board, determine the best outcome for the player specified (win/draw/lose) and all of the moves that would achieve this outcome in the current turn, separated by commas, without spaces.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](black_to_play_draw.png)

```
Example Question: Black to play.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'best_outcome': 'draw', 'move_to_get_best_outcome': 'Ke7,Kf7,Rh2+'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4648
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games;Board_Games
- **Application**: Planning
- **Input Format**: User Interface Screenshots
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'best_outcome': 'exact_str_match', 'move_to_get_best_outcome': 'chess_move_list_jaccard_index'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'best_outcome': 1, 'move_to_get_best_outcome': 4}}
  - **Response Parse Function**: json
- **Source Description**: Endgames created by human annotator and data collected from [https://syzygy-tables.info](https://syzygy-tables.info/), and the questions and answers are adapted to match Jaccard index
