# Task: app_interactive_operations_zoom

## Task Description:

```
Zoom is an online meeting app. In the following set of ten images, each red box highlights a different functional button on the Zoom interface. Based on my instructions, please select the number corresponding to the image of the button I should click, ranging from 1 to 16.
```

![Image](WX20240801-185517@2x.png)

![Image](WX20240801-185707@2x.png)

![Image](WX20240801-185748@2x.png)

![Image](WX20240801-185820@2x.png)

![Image](WX20240801-185843@2x.png)

![Image](WX20240801-185909@2x.png)

![Image](WX20240801-185933@2x.png)

![Image](WX20240801-190033@2x.png)

![Image](WX20240801-190057@2x.png)

![Image](WX20240801-190126@2x.png)

![Image](WX20240903-224748@2x.png)

![Image](WX20240903-224811@2x.png)

![Image](WX20240903-224850@2x.png)

![Image](WX20240903-224908@2x.png)

![Image](WX20240903-224937@2x.png)

![Image](WX20240903-225020@2x.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
Example Question: Initiate a new live video conference session where participants can join to communicate in real-time.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5330
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning;GUI_Operation
- **App**: Planning
- **Input Format**: User Interface Screenshots
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
