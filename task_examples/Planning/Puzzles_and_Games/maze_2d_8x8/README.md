# Task: maze_2d_8x8

## Task Description:

```
Solve the following maze with size of 8x8. You start at the top, one square outside the maze entrance and your goal is to get to the bottom, one square outside the maze. Each move is one sqaure in the 8x8 grids. Write out the sequence of WASD moves (W: up, A: left, S:down, D: right) that would be needed to solve the maze. Your solution must include the one move required to enter the maze and the one move required to exit the maze. The correct answer is shorter than 30.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: SWWSSDSSDSDDWDDSSASAAS
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5541
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games
- **App**: Planning
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'solution': 'exact_str_match_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'solution': 1}}
  - **Response Parse Function**: answer_string
