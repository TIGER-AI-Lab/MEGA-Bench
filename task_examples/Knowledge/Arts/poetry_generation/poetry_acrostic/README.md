# Task: poetry_acrostic

## Task Description:

```
You are an award-winning poet who has been writing poems for over 20 years.

Please write an acrostic poem about the attached image, using the letters in the specified word or words to start off the first letter of each line in the poem. A space between the words indicates a newline. If there are no spaces, there should not be any blank lines. No title is needed.
```

## The 1-shot Example for Task Demonstration:



## Additional Task Information:

- **ID**: 5080
- **Eval Context**: {'acrostic': 'hamster', 'contain': '[hamster, paw, tail, whisker, seed, rodent, scurry, fur]'}
- **Taxonomy Tree Path**: Knowledge;Arts;poetry_generation
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##poem': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##poem': 1}}
  - **Response Parse Function**: dummy
