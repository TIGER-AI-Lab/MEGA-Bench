# Task: Autorater aesthetics

## Task Description:

```
You need assess which image is more aesthetically pleasing or realistic? Answer with "image 1" or "image 2".
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](e1_left.png)

![Image](e1_right.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: image 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5583
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Metrics;Generated_Image_Eval
- **Application**: Metrics
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were collected from ImagenHub. Questions and answers adapted by the annotator
