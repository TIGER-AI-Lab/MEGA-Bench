# Task: muma_theory_of_mind_social_goal

## Task Description:

```
You will see 20 frames from a video, in chronological order. Please answer the question based on the image frames.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1_0.png)

![Image](1_1.png)

![Image](1_2.png)

![Image](1_3.png)

![Image](1_4.png)

![Image](1_5.png)

![Image](1_6.png)

![Image](1_7.png)

![Image](1_8.png)

![Image](1_9.png)

![Image](1_10.png)

![Image](1_11.png)

![Image](1_12.png)

![Image](1_13.png)

![Image](1_14.png)

![Image](1_15.png)

![Image](1_16.png)

![Image](1_17.png)

![Image](1_18.png)

![Image](1_19.png)

```
Example Question: Given the above interaction, assuming that Jessica knows what is inside the fridge, which of the following statements is MOST likely?

When giving information, Jessica has been trying to prevent Michael from finding the juice
When giving information, Jessica has been trying to help Michael locate the juice
When giving information, Jessica was indifferent towards Michael's goals
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: When giving information, Jessica has been trying to help Michael locate the juice
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1474
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;Human_and_Culture;theory_of_minds
- **App**: Knowledge
- **Input Format**: Videos
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
