# Task: recover_masked_word_in_figure

## Task Description:

```
Given a scientific figure/diagram taken from an academic paper, a word or phrase in the image is masked (in black). Your task is to infer the masked word in the given image.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Instructon
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2084
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Diagram
- **App**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
