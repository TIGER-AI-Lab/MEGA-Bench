# Task: Egocentric spatial reasoning

## Task Description:

```
Determine the relative positions of the objects in the picture. Your answer should be a word or short phrase.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: In the egocentric coordinate frame of the image, where is the red chili pepper in relation to the yellow chili pepper?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: right
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1314
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Spatial_Understanding
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'multi_ref_phrase'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data are collected from Epic-Kitchen and the Internet. Questions and answers are adapted for contextual formatted output
