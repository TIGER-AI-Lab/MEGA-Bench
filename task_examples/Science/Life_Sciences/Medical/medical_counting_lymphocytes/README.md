# Task: medical_counting_lymphocytes

## Task Description:

```
Given the medical image, please answer how many lymphocytes are present in the given image?
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](3961_17.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 17
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3398
- **Eval Context**: {}
- **Taxonomy Tree Path**: Science;Life_Sciences;Medical
- **App**: Science
- **Input Format**: Text-Based Images and Documents
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
