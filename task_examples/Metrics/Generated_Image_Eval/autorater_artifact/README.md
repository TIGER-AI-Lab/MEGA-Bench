# Task: Autorater artifact

## Task Description:

```
Please identify whether this image contains any artifacts or not. Please output "yes" or "no"
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](Figure1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: no
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5639
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Metrics;Generated_Image_Eval
- **Application**: Metrics
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'output': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'output': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were collected from ImagenHub. Questions and answers adapted by the annotator
