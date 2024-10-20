# Task: visual_correspondance_in_two_images

## Task Description:

```
Given query reference image (first image) and target image (second image). You are asked to find out which two circled regions of the target image have the same or similar visual content to the two reference circled ones (REF1 and REF2) in the query reference image. The answer should a dictionary that is {'Ref1': 'choice letter 1', 'Ref2': 'choice letter 2'}. The choice letter should be selected from (A, B, C, D).
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](test_Visual_Correspondence_11_1.png)

![Image](test_Visual_Correspondence_11_2.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'Ref1': 'C', 'Ref2': 'A'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3084
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Spatial_Understanding
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'dict_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
