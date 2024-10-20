# Task: app_interactive_operations_ppt

## Task Description:

```
The ten images below each feature a red box highlighting different function buttons on the Microsoft Powerpoint  interface. Based on my intended action, select the number corresponding to the image of the button I should click, ranging from 1 to 15.
```

![Image](WX20240803-131835@2x.png)

![Image](WX20240803-131857@2x.png)

![Image](WX20240803-131925@2x.png)

![Image](WX20240803-132022@2x.png)

![Image](WX20240803-132056@2x.png)

![Image](WX20240803-132115@2x.png)

![Image](WX20240803-132157@2x.png)

![Image](WX20240803-132231@2x.png)

![Image](WX20240803-132248@2x.png)

![Image](WX20240803-132304@2x.png)

![Image](WX20240915-225346@2x.png)

![Image](WX20240915-225402@2x.png)

![Image](WX20240915-225419@2x.png)

![Image](WX20240915-225441@2x.png)

![Image](WX20240915-225536@2x.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
Example Question: Modify the font style of the selected text to enhance readability or match design aesthetics. Choose from a variety of typefaces available in the font dropdown menu.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5271
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning;GUI_Operation
- **App**: Planning
- **Input Format**: User Interface Screenshots
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
