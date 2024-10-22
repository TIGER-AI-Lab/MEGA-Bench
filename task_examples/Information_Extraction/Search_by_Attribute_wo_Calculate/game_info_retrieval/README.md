# Task: Game info retrieval

## Task Description:

```
Given a set of screenshots from a game information page and a specific query, retrieve the names of the games that match the query.  If there are multiple matching games, provide a list of game names separated by commas.
```

![Image](game_info_retrieval1.png)

![Image](game_info_retrieval2.png)

![Image](game_info_retrieval3.png)

![Image](game_info_retrieval4.png)

![Image](game_info_retrieval5.png)

![Image](game_info_retrieval6.png)

![Image](game_info_retrieval7.png)

![Image](game_info_retrieval8.png)

![Image](game_info_retrieval9.png)

![Image](game_info_retrieval10.png)

![Image](game_info_retrieval11.png)

![Image](game_info_retrieval12.png)

![Image](game_info_retrieval13.png)

![Image](game_info_retrieval14.png)

![Image](game_info_retrieval15.png)

## The 1-shot Example for Task Demonstration:

## Example Query:

```
Question: Find the game with a price less than $10.
```

```
Demonstration example(s) of the task:
Example 1:
Example Question: Find the game with a rating of 4.8 or higher.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Ghost of Tsushima DIRECTOR'S CUT, Titanfall® 2: Ultimate Edition, Hades II, SnowRunner
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1627
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Search_by_Attribute_wo_Calculate
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'str_set_equality_comma'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Screenshots were taken by the human annotator on the [Epic Games Store](https://store.epicgames.com/). Questions and answers were created by the annotator.
