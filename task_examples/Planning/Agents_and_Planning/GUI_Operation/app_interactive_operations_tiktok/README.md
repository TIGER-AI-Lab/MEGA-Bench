# Task: app_interactive_operations_tiktok

## Task Description:

```
The ten images below each feature a red box highlighting different function buttons on the TikTok interface. Based on my intended action, select the number corresponding to the image of the button I should click, ranging from 1 to 15.
```

![Image](WX20240802-214811@2x.png)

![Image](WX20240802-214828@2x.png)

![Image](WX20240802-214930@2x.png)

![Image](WX20240802-214947@2x.png)

![Image](WX20240802-215010@2x.png)

![Image](WX20240802-215054@2x.png)

![Image](WX20240802-215121@2x.png)

![Image](WX20240802-215137@2x.png)

![Image](WX20240802-215205@2x.png)

![Image](WX20240802-215234@2x.png)

![Image](WX20240915-232359@2x.png)

![Image](WX20240915-232421@2x.png)

![Image](WX20240915-232437@2x.png)

![Image](WX20240915-232513@2x.png)

![Image](WX20240915-232550@2x.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
Example Question: Click this button to show I enjoy this video, helping it gain more visibility.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5257
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning;GUI_Operation
- **App**: Planning
- **Input Format**: User Interface Screenshots
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
