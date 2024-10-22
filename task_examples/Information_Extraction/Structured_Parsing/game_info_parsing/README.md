# Task: Game info parsing

## Task Description:

```
Given a screenshot of a game information page, extract the following details: 

(1) Game name 
(2) Rating 
(3) Current Price 
(4) Refund type 
(5) Developer 
(6) Publisher 
(7) Release date 
(8) Initial Release
(9) Platform (Windows, Mac)
(10) Genres 
(11) Features. 

If any of the above details are not present in the image, leave the corresponding field blank.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](game_info_parsing1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'name': 'Need for Speed™ Heat Deluxe Edition', 'rating': '4.6', 'price': '$6.99', 'refund': 'Self-Refundable', 'developer': 'Ghost Games', 'publisher': 'Electronic Arts', 'date': '03/28/24', 'initial': '11/08/19', 'platform': 'Windows', 'genres': 'Action, Racing', 'features': 'Co-op, Online Multiplayer, Single Player'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 954
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Structured_Parsing
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'name': 'simple_str_match', 'rating': 'simple_str_match', 'price': 'simple_str_match', 'date': 'simple_str_match', 'refund': 'simple_str_match', 'developer': 'simple_str_match', 'publisher': 'simple_str_match', 'features': 'simple_str_match', 'genres': 'simple_str_match', 'platform': 'simple_str_match', 'initial': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'name': 1, 'rating': 1, 'price': 1, 'date': 1, 'refund': 1, 'developer': 1, 'publisher': 1, 'features': 1, 'genres': 1, 'platform': 1, 'initial': 1}}
  - **Response Parse Function**: json
- **Source Description**: Screenshots were taken by the human annotator on the [Epic Games Store](https://store.epicgames.com/). Questions and answers were created by the annotator.
