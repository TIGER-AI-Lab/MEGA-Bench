# Task: pictionary_chinese_food_img2en

## Task Description:

```
What is the name of the Chinese dish in the picture? Follow the hint in the text to answer the question. Each * in the hint is a letter.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: Hint: M*** T***
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Mapo Tofu
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 6362
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games;Pictionary
- **App**: Planning
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
