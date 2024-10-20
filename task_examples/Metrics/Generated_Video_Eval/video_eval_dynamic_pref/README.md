# Task: video_eval_dynamic_pref

## Task Description:

```
Here we provide some frames of AI-generated videos from Diffusion models, please select the video with better dynamic degree. 

 Below are frames of two videos, by default there will be 16 images, the first 8 images are from the first video, the second 8 frames from the second video if there's no other special statement. Please choose the one with better 'Visual Quality' as defined above, using format "Answer: $CHOICE", $CHOICE is A for the first video, B for the second.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](7_00.png)

![Image](7_01.png)

![Image](7_02.png)

![Image](7_03.png)

![Image](7_04.png)

![Image](7_05.png)

![Image](7_06.png)

![Image](7_07.png)

![Image](9_00.png)

![Image](9_01.png)

![Image](9_02.png)

![Image](9_03.png)

![Image](9_04.png)

![Image](9_05.png)

![Image](9_06.png)

![Image](9_07.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: A
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3849
- **Eval Context**: {}
- **Taxonomy Tree Path**: Metrics;Generated_Video_Eval
- **App**: Metrics
- **Input Format**: Videos
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
