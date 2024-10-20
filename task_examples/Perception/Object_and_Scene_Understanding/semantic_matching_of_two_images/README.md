# Task: semantic_matching_of_two_images

## Task Description:

```
Given query reference image with two reference circles (REF1 and REF2) and target image with four choice circles (A, B, C, D). You are asked to find circles in the target image that have the same semantic information as the ones in the reference image. The answer should be a dictionary that is {'Ref1': 'choice letter 1', 'Ref2': 'choice letter 2'}. The choice letter should be selected from (A, B, C, D).
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](val_Semantic_Correspondence_124_2.png)

![Image](val_Semantic_Correspondence_124_1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'Ref1': 'C', 'Ref2': 'D'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4270
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Object_and_Scene_Understanding
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'dict_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
