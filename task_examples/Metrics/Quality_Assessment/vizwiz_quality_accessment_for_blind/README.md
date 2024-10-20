# Task: vizwiz_quality_accessment_for_blind

## Task Description:

```
In this task, you are an asisstant to a visual dispaird user, who is going to use the phone's camera to capture a image. Your mision is to access the quality of the captured image, and classify it into the following categories: (1) BLR: Image too blurry; (2) BRT: Image too bright, likely overexposure; (3) DRK: Image too dark, likely underexposure; (4) FRM: improper framing; (5) OBS: obstruction; (6) ROT: rotated views; (7) NON: no flaws are detected. Now, following presents one example for each category, please refer to them and recognize the target image (the last image). Output all the possible visual flaws you detected.
```

![Image](BLR_example.png)

![Image](BRT_example.png)

![Image](DRK_example.png)

![Image](FRM_example.png)

![Image](OBS_example.png)

![Image](ROT_example.png)

![Image](NON_example.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: NON
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1970
- **Eval Context**: {}
- **Taxonomy Tree Path**: Metrics;Quality_Assessment
- **App**: Metrics
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'set_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
