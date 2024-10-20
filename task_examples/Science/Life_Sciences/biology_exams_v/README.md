# Task: biology_exams_v

## Task Description:

```
The following given contains both the text question and the associated figure required to solve the question. Your task is to answer the question in the image. Each question is provided with a few options, where you should answer with the option letter. For multiple-choice questions, only answer the choice letter with format "Answer: $CHOICE_LETTER ".
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](image_1.png)

```
Example Question: The answer is a letter
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: A
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1397
- **Eval Context**: {}
- **Taxonomy Tree Path**: Science;Life_Sciences
- **App**: Science
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
