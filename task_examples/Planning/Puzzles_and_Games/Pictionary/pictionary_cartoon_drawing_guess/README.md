# Task: pictionary_cartoon_drawing_guess

## Task Description:

```
Given a drawing and a text hint, guess what the drawing represents.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: Hint: It's an object, 2 words, 11 letters.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: roller skate
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 6348
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games;Pictionary
- **App**: Planning
- **Input Format**: Artistic and Creative Content
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
