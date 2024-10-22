# Task: Meme explain

## Task Description:

```
Explain a popular internet meme to someone who is unfamiliar with online culture
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Response: Answer: “Distracted boyfriend” first entered the meme game in 2017, when a Turkish Facebook group used a stock photo of a man walking with a girl while checking out another girl to make a joke about Phil Collins. The meme continues to be relevant today while being used as inspiration for pop culture references, such as this recent one involving “Queer Eye’s” Antoni Porowski, and new celebrity couple Kate Beckinsale and Pete Davidson at a New York Rangers game.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Information:

- **Sample ID**: 605
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
