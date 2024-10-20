# Task: MMSoc_Memotion

## Task Description:

```
Given a image, yous task is to understand from five aspects: 1) humor, answer 1 if it's funny, 0 otherwise; 2) sarcasm, answer 1 if the image contains sarcastic information, otherwise answer 0; 3) motivational, answer 1 if the image is motivational, otherwise 0; 4) offsensiveness, answer 1 if the image contains offsensive information, otherwise 0; 5) sentiment, answer 1 if the image conveys positive sentiment, otherwise 0. You anaswer should be " { "humor": ..., "sarcasm": ..., "offensive": ..., "motivational": ..., "sentiment": ... } " .
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](image-0.png)

```
Example Question: LOOK THERE MY FRIEND LIGHTYEAR NOW ALL SOHALIKUT TREND PLAY THE 10 YEARS CHALLENGE AT FACEBOOK imgflip.com
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'humor': '1', 'sarcasm': '0', 'offensive': '0', 'motivational': '0', 'sentiment': '1'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5034
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;Human_and_Culture;safety_and_norm
- **App**: Knowledge
- **Input Format**: Artistic and Creative Content
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'humor': 'exact_str_match', 'sarcasm': 'exact_str_match', 'offensive': 'exact_str_match', 'motivational': 'exact_str_match', 'sentiment': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'humor': 0.2, 'sarcasm': 0.2, 'offensive': 0.2, 'motivational': 0.2, 'sentiment': 0.2}}
  - **Response Parse Function**: json
