# Task: Memorization indian celebrity

## Task Description:

```
Please answer the name and year of birth of the given celebrity.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](diljit-dosanjh.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'name': 'Diljit Dosanjh', 'birth': '1984'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 6476
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Memorization
- **Application**: Knowledge
- **Input Format**: Photographs
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'name': 'multi_ref_phrase', 'birth': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'name': 1, 'birth': 1}}
  - **Response Parse Function**: json
- **Source Description**: Images and labels come from various websites. Questions were created by a human annotator.
