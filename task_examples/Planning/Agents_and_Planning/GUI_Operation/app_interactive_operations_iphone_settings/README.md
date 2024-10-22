# Task: App interactive operations iphone settings

## Task Description:

```
The images below each feature a red box highlighting different function buttons of the Settings interface on an iPhone. Based on my intended action, select the number corresponding to the image of the button I should click, ranging from 1 to 16.
```

![Image](WX20240803-131130@2x.png)

![Image](WX20240803-131349@2x.png)

![Image](WX20240803-131405@2x.png)

![Image](WX20240803-131423@2x.png)

![Image](WX20240803-131442@2x.png)

![Image](WX20240803-131540@2x.png)

![Image](WX20240803-131605@2x.png)

![Image](WX20240803-131620@2x.png)

![Image](WX20240803-131634@2x.png)

![Image](WX20240803-131650@2x.png)

![Image](WX20240902-172517@2x.png)

![Image](WX20240902-172555@2x.png)

![Image](WX20240902-172611@2x.png)

![Image](WX20240902-172625@2x.png)

![Image](WX20240902-172708@2x.png)

![Image](WX20240902-172732@2x.png)

## The 1-shot Example for Task Demonstration:

## Example Query:

```
Question: I've moved to a new home and want to switch my phone's Wi-Fi network
```

```
Demonstration example(s) of the task:
Example 1:
Example Question: Turn off or on airplane mode
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5229
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning;GUI_Operation
- **Application**: Planning
- **Input Format**: User Interface Screenshots
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from application screenshots by human annotator, and the questions and answers are designed by human annotator
