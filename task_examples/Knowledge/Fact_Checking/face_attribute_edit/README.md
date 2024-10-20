# Task: face_attribute_edit

## Task Description:

```
Your task is to determine if the face in the image has been edited by changing the expression or other attributes. You will be give the caption and the image, and you should recognize the scene, identify personal information and detect the correctness of the face status. The answer should follow the format "Answer: $BOOL". $BOOL is 1 if you think the face attribute has been manipulated, $BOOL is 0 otherwise.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1167947_face_attribute.png)

```
Example Question: In 1905 Theodore Roosevelt reformed football perhaps it can be done again
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5443
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;Fact_Checking
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
