# Task: App interactive operations notes

## Task Description:

```
The images below each feature a red box highlighting different function buttons of the Notes app interface on an iPhone. Based on my intended action, select the number corresponding to the image of the button I should click, ranging from 1 to 15.
```

![Image](WX20240803-132400@2x.png)

![Image](WX20240803-132419@2x.png)

![Image](WX20240803-132439@2x.png)

![Image](WX20240803-132453@2x.png)

![Image](WX20240803-132510@2x.png)

![Image](WX20240803-132527@2x.png)

![Image](WX20240803-132544@2x.png)

![Image](WX20240803-132608@2x.png)

![Image](WX20240803-132631@2x.png)

![Image](WX20240803-132702@2x.png)

![Image](WX20240903-223119@2x.png)

![Image](WX20240903-223135@2x.png)

![Image](WX20240903-223149@2x.png)

![Image](WX20240903-223203@2x.png)

![Image](WX20240908-225820@2x.png)

## The 1-shot Example for Task Demonstration:

## Example Query:

```
Question: Send my note to my roommate
```

```
Demonstration example(s) of the task:
Example 1:
Example Question: I made a mistake, undo
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5401
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
