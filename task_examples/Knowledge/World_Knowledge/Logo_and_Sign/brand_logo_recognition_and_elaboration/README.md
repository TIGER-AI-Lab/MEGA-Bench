# Task: brand_logo_recognition_and_elaboration

## Task Description:

```
Identify the brand logo presented in the query image. Also provide the country of origin (i.e., where the company was founded) of the brand. Remove all spaces and hyphens from the brand name. If the image does not contain a logo, answer NA for both fields.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1358914336.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'brand name': 'RedBull', 'country of origin': 'Austria'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Logo_and_Sign
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'brand name': 'multi_ref_phrase', 'country of origin': 'multi_ref_phrase'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'brand name': 1, 'country of origin': 1}}
  - **Response Parse Function**: json
