# Task: Poetry custom rhyming scheme

## Task Description:

```
You are an award-winning poet who has been writing poems for over 20 years.

Please write a poem about the attached image, using the specified rhyming scheme. Exact rhymes are required: near rhymes will be rejected. Do not use the same rhyme for a different letter in the rhyming scheme.e.g. For abab cdcd, a word used for the "d" rhyme cannot rhyme with a word used for the "a" rhyme.

No title is needed.
```

## The 1-shot Example for Task Demonstration:

## Example Query:

![Image](0.png)

```
Question: Rhyming scheme: abba cc
```



## Additional Information:

- **Sample ID**: 5110
- **Eval Context (for this query sample)**: {'rhyming_scheme': 'abba cc', 'contain': '[hamster, paw, tail, whisker, seed, rodent, scurry, fur]'}
- **Taxonomy Tree Path**: Knowledge;Arts;poetry_generation
- **Application**: Knowledge
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##poem': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##poem': 1}}
  - **Response Parse Function**: dummy
- **Source Description**: Images come from various websites. Questions and evaluation constraints were created by a human annotator.
