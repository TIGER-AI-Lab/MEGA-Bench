# Task: poetry_petrarchian_sonnet_optional_meter

## Task Description:

```
You are an award-winning poet who has been writing poems for over 20 years.

Please write a Petrarchian Sonnet about the attached image. You will be evaluated on both the rhyming scheme and number of syllables (10-12 per line), but you may ignore the requirement to use iambic pentameter. Exact rhymes are required: near rhymes will be rejected. Do not use the same rhyme for a different letter in the rhyming scheme.e.g. For abab cdcd, a word used for the "d" rhyme cannot rhyme with a word used for the "a" rhyme.

Put a blank line between each quatrain and the sestet (use the CDCDCD sextet) but nowhere else. Do not split the sestet into two tercets.

No title is needed.
```

## The 1-shot Example for Task Demonstration:



## Additional Task Information:

- **ID**: 5125
- **Eval Context**: {'contain': '[hamster, paw, tail, whisker, seed, rodent, scurry, fur]', 'syllables': '[10,12][10,12][10,12][10,12] [10,12][10,12][10,12][10,12] [10,12][10,12][10,12][10,12][10,12][10,12]', 'rhyming_scheme': 'abba abba cdcdcd'}
- **Taxonomy Tree Path**: Knowledge;Arts;poetry_generation
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##poem': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##poem': 1}}
  - **Response Parse Function**: dummy
