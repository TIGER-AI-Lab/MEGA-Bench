# Task: pictionary_skribbl_io

## Task Description:

```
You are playing a game of Pictionary. Guess the word from the illustration and the word hint at the top of the screenshot. The words in the word bubbles on the left are guesses from other players: you may ignore them if you like.
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
Answer: exit
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 6299
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games;Pictionary
- **App**: Planning
- **Input Format**: Artistic and Creative Content
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'word': 'exact_str_match_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'word': 1}}
  - **Response Parse Function**: answer_string
