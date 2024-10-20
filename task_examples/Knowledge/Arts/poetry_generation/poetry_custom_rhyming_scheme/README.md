# Task: poetry_custom_rhyming_scheme

## Task Description:

```
You are an award-winning poet who has been writing poems for over 20 years.

Please write a poem about the attached image, using the specified rhyming scheme. Exact rhymes are required: near rhymes will be rejected. Do not use the same rhyme for a different letter in the rhyming scheme.e.g. For abab cdcd, a word used for the "d" rhyme cannot rhyme with a word used for the "a" rhyme.

No title is needed.
```

## The 1-shot Example for Task Demonstration:



## Additional Task Information:

- **ID**: 5110
- **Eval Context**: {'rhyming_scheme': 'abba cc', 'contain': '[hamster, paw, tail, whisker, seed, rodent, scurry, fur]'}
- **Taxonomy Tree Path**: Knowledge;Arts;poetry_generation
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##poem': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##poem': 1}}
  - **Response Parse Function**: dummy
