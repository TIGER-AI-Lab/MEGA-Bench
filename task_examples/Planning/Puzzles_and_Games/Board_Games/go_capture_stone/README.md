# Task: go_capture_stone

## Task Description:

```
We are playing the "capture stone" practice in Go. You need to answer the location of the expected next move of the black stone, so that you can capture a white stone before yourself being captured. The answer should be the column index followed by the row index.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](example-1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: E4
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3039
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games;Board_Games
- **App**: Planning
- **Input Format**: Artistic and Creative Content
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'location of the next move': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'location of the next move': 1}}
  - **Response Parse Function**: answer_string