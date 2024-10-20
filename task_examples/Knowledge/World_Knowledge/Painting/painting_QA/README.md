# Task: painting_QA

## Task Description:

```
Watch the following one or more paintings, answer the corresponding question.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: What style are the following painting in? Choose from ["Renaissance", "Cubism", "Impression", "Realism", "Abstract", ""]
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Impression
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2491
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Painting
- **App**: Knowledge
- **Input Format**: Artistic and Creative Content
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
