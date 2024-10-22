# Task: Poetry shakespearean sonnet

## Task Description:

```
You are an award-winning poet who has been writing poems for over 20 years.

Please write a Shakespearean Sonnet about the attached image. You will be evaluated on the rhyming scheme, the number of syllables (10 per line), and whether iambic pentameter is used.

Exact rhymes are required: near rhymes will be rejected. Do not use the same rhyme for a different letter in the rhyming scheme.e.g. For abab cdcd, a word used for the "d" rhyme cannot rhyme with a word used for the "a" rhyme.

Put a blank line between each quatrain and the concluding couplet but nowhere else.

No title is needed.
```

## The 1-shot Example for Task Demonstration:

## Example Query:

![Image](0.png)



## Additional Information:

- **Sample ID**: 5155
- **Eval Context (for this query sample)**: {'contain': '[hamster, paw, tail, whisker, seed, rodent, scurry, fur]', 'syllables': '[10][10][10][10] [10][10][10][10] [10][10][10][10] [10][10]', 'rhyming_scheme': 'abab cdcd efef gg', 'poetry_meter': 'iambic'}
- **Taxonomy Tree Path**: Knowledge;Arts;poetry_generation
- **Application**: Knowledge
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##poem': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##poem': 1}}
  - **Response Parse Function**: dummy
- **Source Description**: Images come from various websites. Questions and evaluation constraints were created by a human annotator.
