# Task: medical_polyp_segmentation_single_object_rater

## Task Description:

```
There is a set of images where the first one is medical image with polyps and the remaining ones are segmentation mask images for indentifying the polyps. You are asked to rate the quality of segmentation mask images and list the indexes of mask images from best to worst. The answer should be a list including image indexes and the index should be from A: second image, B: third image, and C: fourth image.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](web-1.png)

![Image](web-1-1.png)

![Image](web-1-2.png)

![Image](web-1-3.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: ['A', 'B', 'C']
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2788
- **Eval Context**: {}
- **Taxonomy Tree Path**: Science;Life_Sciences;Medical
- **App**: Science
- **Input Format**: Text-Based Images and Documents
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'sequence_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
