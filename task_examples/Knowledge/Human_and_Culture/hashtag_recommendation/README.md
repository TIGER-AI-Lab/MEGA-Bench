# Task: Hashtag recommendation

## Task Description:

```
Given a piece of text from social media and its corresponding image, you need to select all the possible hashtags from a provided set of hashtags.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1_1.png)

```
Example Question: Text: Did any body beat this guy brh I challenge him first time! He's impossible to beat but still I did it guys.
Hashtag candidates: #PS5Share, #Olympics2024, #PS5, #BlackMythWokong, #Zelda
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: [#PS5Share, #PS5, #BlackMythWokong]
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4326
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;Human_and_Culture
- **Application**: Knowledge
- **Input Format**: Photographs
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'hashtags': 'set_precision'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'hashtags': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images and hashtags come from various social media websites. Questions were created by a human annotator.
