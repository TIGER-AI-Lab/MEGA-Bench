# Task: Distinguish ai generated image

## Task Description:

```
Your task is to figure out whether an image is AI generated or human captured. Your answer should be one of the following: AI generated, Human captured.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](036867701fd244ee99401e86c62546a4df8c8f8c0b48cdf2d0cbf1c895b83f11.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: AI generated
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4554
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;Fact_Checking
- **Application**: Knowledge
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images come from various websites and image generators. Questions and annotations were created by a human annotator.
