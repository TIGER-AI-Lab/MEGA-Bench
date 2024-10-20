# Task: entertainment_web_game_style

## Task Description:

```
Given the query webpage screenshot, you are asked to answer 1. the game style of the given image. The answer should be selected from the list ['Sports', 'Action', 'Role-Playing', 'Strategy', 'Adventure', 'Shooter','Racing'], 2. the publisher's name for the query game
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](293.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'Answer': 'Shooter', 'Publisher': 'Krafton'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4002
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Structured_Parsing
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match', 'Publisher': 'exact_str_match_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1, 'Publisher': 1}}
  - **Response Parse Function**: json
