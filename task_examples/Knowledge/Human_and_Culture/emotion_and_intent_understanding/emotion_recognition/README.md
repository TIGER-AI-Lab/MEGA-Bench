# Task: Emotion recognition

## Task Description:

```
Recognize the human emotions in the provided images. There are seven possible emotions: anger, disgust, fear, happy, sad, surprise, and neutral.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1_1.png)

![Image](1_2.png)

![Image](1_3.png)

![Image](1_4.png)

![Image](1_5.png)

![Image](1_6.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: anger
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 689
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;Human_and_Culture;emotion_and_intent_understanding
- **Application**: Knowledge
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'emotion': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'emotion': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Videos and labels come from the CAER dataset. Questions and answers were adapted by a human annotator.
