# Task: next_action_prediction

## Task Description:

```
Based on the given images from a video, predict the person's next action. You must choose your answer from the choice list.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1_0.png)

![Image](1_1.png)

![Image](1_4.png)

![Image](1_5.png)

![Image](1_6.png)

![Image](1_7.png)

![Image](1_8.png)

![Image](1_12.png)

![Image](1_13.png)

![Image](1_14.png)

```
Example Question: Choose the answer from "Throw the blanket", "Eat the medicine", "Open the door", "Turn off the light", "Lie on the sofa/couch", "Put down the box".
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Throw the blanket
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1082
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Temporal_Understanding
- **App**: Perception
- **Input Format**: Videos
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
