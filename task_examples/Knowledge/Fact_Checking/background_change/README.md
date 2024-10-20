# Task: background_change

## Task Description:

```
Your task is to determine if the time and location of an event align with the actual scene, focusing on the checing if the background of the image has been manipulated or not. You will be give the caption and image. The answer should follow the format "Answer: $BOOL". $BOOL is 1 if you think the background of the image has been manipulated and is not aligned with the text, otherwise $BOOL is 0.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](452276.png)

```
Example Question: The relationship between Chris Froome left and Sir Bradley Wiggins has been strained since Froome was chosen to lead Team Sky at this year s Tour de France
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 0
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5429
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;Fact_Checking
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
