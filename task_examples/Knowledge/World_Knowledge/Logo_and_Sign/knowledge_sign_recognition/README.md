# Task: Knowledge sign recognition

## Task Description:

```
In the following, you are presented with a multi-choice visual question, please select all the correct answers to the question (separated by comma).
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](stop_sign_1.png)

![Image](stop_sign_2.png)

![Image](stop_sign_3.png)

![Image](stop_sign_4.png)

![Image](stop_sign_5.png)

```
Example Question: Which of the following is not a legitimate STOP sign? Answer the image index from 1 to 5.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 4
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3412
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Logo_and_Sign
- **Application**: Knowledge
- **Input Format**: Text-Based Images and Documents
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'str_set_equality_comma'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images come from various websites. Questions were created by a human annotator.
