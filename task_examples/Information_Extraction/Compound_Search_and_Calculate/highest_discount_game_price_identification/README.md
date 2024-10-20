# Task: highest_discount_game_price_identification

## Task Description:

```
Find the price of the game with the highest discount on a Steam discount recommendation page, using both textual information and visual discount indicators.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](highest_discount_game_price_identification1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 4.50
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4453
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Compound_Search_and_Calculate
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
