# Task: poetry_limerick

## Task Description:

```
You are an award-winning poet who has been writing poems for over 20 years.

Please write a Limerick about the attached image. You will be evaluated on both the rhyming scheme and number of syllables. Exact rhymes are required: near rhymes will be rejected. No title is needed.
```

## The 1-shot Example for Task Demonstration:



## Additional Task Information:

- **ID**: 5095
- **Eval Context**: {'contain': '[hamster, paw, tail, whisker, seed, rodent, scurry, fur]', 'syllables': '[7,10][7,10][5,7][5,7][7,10]', 'rhyming_scheme': 'aabba'}
- **Taxonomy Tree Path**: Knowledge;Arts;poetry_generation
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##poem': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##poem': 1}}
  - **Response Parse Function**: dummy
