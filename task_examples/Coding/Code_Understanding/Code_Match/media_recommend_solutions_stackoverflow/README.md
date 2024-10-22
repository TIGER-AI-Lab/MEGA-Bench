# Task: Media recommend solutions stackoverflow

## Task Description:

```
Given the proposed question in the first sceenshot image and the candidate responses from the remainning three images, please recommend which response is more helpful based on the response content and others' votes. The answer should be choice letter from A: second image, B: third image, and C: fourth image
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](web-1-1.png)

![Image](web-1-2.png)

![Image](web-1-3.png)

![Image](web-1-4.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: A
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4016
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Coding;Code_Understanding;Code_Match
- **Application**: Coding
- **Input Format**: User Interface Screenshots
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data are collected from Stack Overflow Website, and the question and answer are adapted to match string
