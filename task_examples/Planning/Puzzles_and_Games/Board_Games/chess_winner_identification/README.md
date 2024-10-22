# Task: Chess winner identification

## Task Description:

```
You are given a visual representation of a chess game for which the outcome of the game is determinable, assuming both sides take the best moves.
YOUR TASK is to task is to analyze a given chess game representation and identify the winner.
Respond with "White", "Black", "Draw" on whether the game resulted in a win for White or Black, or if it ended without a winner.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](w_1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: White
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 703
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games;Board_Games
- **Application**: Planning
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from IsoBench, and the questions and answers are adapted by human annotator
