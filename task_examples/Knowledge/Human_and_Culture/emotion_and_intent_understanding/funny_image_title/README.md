# Task: Funny image title

## Task Description:

```
Generate a short title for this funny image.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Response: Answer: Please put the long dog down, balloons.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Information:

- **Sample ID**: 490
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;Human_and_Culture;emotion_and_intent_understanding
- **Application**: Knowledge
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images come from various websites. Questions were created by a human annotator.
