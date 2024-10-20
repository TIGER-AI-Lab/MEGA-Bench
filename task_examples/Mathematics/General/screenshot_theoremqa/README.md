# Task: screenshot_theoremqa

## Task Description:

```
You need to answer a science question and then return your answer in the \boxed{..}.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](f1.png)

```
Example Question: What's the answer of Q1?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: \boxed{11760}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5185
- **Eval Context**: {}
- **Taxonomy Tree Path**: Mathematics;General
- **App**: Mathematics
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'boxed_single_numerical_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: verbatim_answer_string
