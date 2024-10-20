# Task: code_add_tag

## Task Description:

```
Given the code segment in the image, choose the right tags for it from the provided tag options.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1-1.png)

![Image](1-2.png)

![Image](1-3.png)

```
Example Question: Choose from: binary search, hashing, data structures, combinatorics , bitmasks
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: binary search, data structures
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2476
- **Eval Context**: {}
- **Taxonomy Tree Path**: Coding;Code_Understanding
- **App**: Coding
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'set_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
