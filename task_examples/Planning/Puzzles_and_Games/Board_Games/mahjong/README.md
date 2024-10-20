# Task: mahjong

## Task Description:

```
Review the current Mahjong tiles in the hand. Based on the hand's structure, identify which tiles would complete a winning combination if drawn. Once the waiting tiles are identified, sort them in the following order: Dots from smallest to largest, Bamboo from smallest to largest, Characters from smallest to largest, Winds in the order of East, South, West, North, and finally, Dragons in the order of Red, Green, White.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0.jpg)

```
Example Question: Which tile(s) is this hand waiting for?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 6 Dots, 4 Characters
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3547
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games;Board_Games
- **App**: Planning
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Waiting for': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Waiting for': 1}}
  - **Response Parse Function**: answer_string
