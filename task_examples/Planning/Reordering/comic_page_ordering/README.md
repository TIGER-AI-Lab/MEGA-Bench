# Task: comic_page_ordering

## Task Description:

```
Given multiple consecutive but shuffled pages from a comic book, your task is to reorder the pages to reflect the correct narrative sequence.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1_5.png)

![Image](1_2.png)

![Image](1_1.png)

![Image](1_3.png)

![Image](1_4.png)

![Image](1_6.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 3,2,4,5,1,6
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3333
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Reordering
- **App**: Planning
- **Input Format**: Artistic and Creative Content
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'order': 'sequence_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'order': 1}}
  - **Response Parse Function**: answer_string
