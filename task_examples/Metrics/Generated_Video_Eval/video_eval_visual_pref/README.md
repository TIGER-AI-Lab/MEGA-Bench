# Task: video_eval_visual_pref

## Task Description:

```
Here we provide some frames of AI-generated videos from Diffusion models, please select the video with better 'Visual Quality'. The differences between Good and Bad 'Visual Quality' are as follows: 
Good: (1) The video looks clear and normal on its appearance.
(2) The features like Brightness, Contrast, Color, etc, are appropriate and stable.
 Bad: (1) local obvious unclear or blurry
(2) too low resolution
(3) some speckles or black patches
(4) appearance of video is skewed and distorted
(5) unstable optical property, such as brightness, contrast, saturation, exposure etc
(6) flickering color of main objects and background.

 Below are frames of two videos, by default there will be 16 images, the first 8 images are from the first video, the second 8 frames from the second video if there's no other special statement. Please choose the one with better 'Visual Quality' as defined above using format "Answer: $CHOICE", where $CHOICE is A for the first video, B for the second.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0_00.png)

![Image](0_01.png)

![Image](0_02.png)

![Image](0_03.png)

![Image](0_04.png)

![Image](0_05.png)

![Image](0_06.png)

![Image](0_07.png)

![Image](1_00.png)

![Image](1_01.png)

![Image](1_02.png)

![Image](1_03.png)

![Image](1_04.png)

![Image](1_05.png)

![Image](1_06.png)

![Image](1_07.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: A
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3068
- **Eval Context**: {}
- **Taxonomy Tree Path**: Metrics;Generated_Video_Eval
- **App**: Metrics
- **Input Format**: Videos
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
