# Task: nlvr2_two_image_compare_qa

## Task Description:

```
Each image contains two sub-images (left and right). Answer a question by understanding and comparing the two sub-images.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: For which displayed image, the sentence 'One image contains two curved stairways with carpeted steps, white base boards, and brown handrails and balusters, and at least one of the stairways has white spindles.' holds?  Answer left or right
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: left
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1182
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Object_and_Scene_Understanding
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'multi_ref_phrase'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
