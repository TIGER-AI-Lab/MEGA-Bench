# Task: mvsa_sentiment_classification

## Task Description:

```
Given an image and text pair collected from social media, your task is to determine the sentiment type of the pair. There are three sentiment types: positive, negative, and neutral.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: ""I think it's time for change"" - Ana Commit to Vote: #GenerationTrudeau #SFU #LPC #elxn42
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: positive
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1286
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;Human_and_Culture;emotion_and_intent_understanding
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'sentiment type': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'sentiment type': 1}}
  - **Response Parse Function**: answer_string
