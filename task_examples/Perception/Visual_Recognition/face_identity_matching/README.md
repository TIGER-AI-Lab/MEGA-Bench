# Task: Face identity matching

## Task Description:

```
This task involves analyzing a set of 5 images to identify which images show the same person. Among the 5 images, there are two pairs of images where each pair shows the same individual, and one image shows a different person. The goal is to determine the matching pairs by providing the indices of the images that depict the same person. The answer should list the smaller indices first within each pair.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1_1.png)

![Image](1_2.png)

![Image](1_3.png)

![Image](1_4.png)

![Image](1_5.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 13,45
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1669
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Visual_Recognition
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'set_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were collected from CelebA. Questions and answers re-designed by the annotator for this specific task
