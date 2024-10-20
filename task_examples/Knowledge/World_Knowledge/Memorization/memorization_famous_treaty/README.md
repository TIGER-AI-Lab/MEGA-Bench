# Task: memorization_famous_treaty

## Task Description:

```
What treaty does this image remind you of and which year was it signed? Please answer with short phrase.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](peace_of_westphalia.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'Name': 'Peace of Westphalia', 'Year': '1648'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 6462
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Memorization
- **App**: Knowledge
- **Input Format**: Artistic and Creative Content
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Name': 'multi_ref_phrase', 'Year': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Name': 1, 'Year': 1}}
  - **Response Parse Function**: json
