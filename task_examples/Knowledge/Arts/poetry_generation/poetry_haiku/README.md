# Task: Poetry haiku

## Task Description:

```
You are an award-winning poet who has been writing poems for over 20 years.

Please write a Haiku poem about the attached image. No title is needed.
```

## The 1-shot Example for Task Demonstration:

## Example Query:

![Image](0.png)



## Additional Information:

- **Sample ID**: 5140
- **Eval Context (for this query sample)**: {'syllables': '575', 'contain': '[hamster, paw, tail, whisker, seed, rodent, scurry, fur]'}
- **Taxonomy Tree Path**: Knowledge;Arts;poetry_generation
- **Application**: Knowledge
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##poem': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##poem': 1}}
  - **Response Parse Function**: dummy
- **Source Description**: Images come from various websites. Questions and evaluation constraints were created by a human annotator.
