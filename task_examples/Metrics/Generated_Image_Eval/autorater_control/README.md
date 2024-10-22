# Task: Autorater control

## Task Description:

```
A model is given an image control signal, like an edge map or keypoints, to produce an output image consistent with the control signal. You need to rate whether the output image is good or not. Answer with "good" or "bad".
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](input_1.png)

![Image](output_1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: bad
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5696
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Metrics;Generated_Image_Eval
- **Application**: Metrics
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'rating': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'rating': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were collected from ImagenHub. Questions and answers adapted by the annotator
