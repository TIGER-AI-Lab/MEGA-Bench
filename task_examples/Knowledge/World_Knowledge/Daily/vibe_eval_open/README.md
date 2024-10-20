# Task: vibe_eval_open

## Task Description:

```
Please answer the given question with a short phrase (1-3 words, no punctuation).
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](figure1.png)

```
Example Question: Which of the four items here is least appropriate for me to drink coffee from?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: cardboard
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 548
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Daily
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'multi_ref_phrase'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
