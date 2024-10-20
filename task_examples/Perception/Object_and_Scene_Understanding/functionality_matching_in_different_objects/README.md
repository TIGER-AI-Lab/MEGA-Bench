# Task: functionality_matching_in_different_objects

## Task Description:

```
Given query reference image (first image) and target image (second image). You are asked to find out which two circled points of the target image have the same or similar functionality to the two circled ones (REF1 and REF2) in the query reference image. The answer should be a dictionary that is {'Ref1': 'choice letter 1', 'Ref2': 'choice letter 2'}. The choice letter should be selected from (A, B, C, D).
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](test_Functional_Correspondence_1_1.png)

![Image](test_Functional_Correspondence_1_2.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'Ref1': 'C', 'Ref2': 'A'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2602
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Object_and_Scene_Understanding
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'dict_precision'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
