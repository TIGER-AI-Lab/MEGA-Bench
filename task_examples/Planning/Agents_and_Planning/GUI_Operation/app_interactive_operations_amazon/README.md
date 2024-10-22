# Task: App interactive operations amazon

## Task Description:

```
The ten images below each feature a red box highlighting different function buttons on the Amazon website. Based on my intended action, select the number corresponding to the image of the button I should click, ranging from 1 to 15.
```

![Image](WX20240803-151303@2x.png)

![Image](WX20240803-151324@2x.png)

![Image](WX20240803-151354@2x.png)

![Image](WX20240803-151412@2x.png)

![Image](WX20240803-151438@2x.png)

![Image](WX20240803-151507@2x.png)

![Image](WX20240803-151532@2x.png)

![Image](WX20240803-151618@2x.png)

![Image](WX20240803-151644@2x.png)

![Image](WX20240803-151715@2x.png)

![Image](WX20240915-221310@2x.png)

![Image](WX20240915-221726@2x.png)

![Image](WX20240915-221751@2x.png)

![Image](WX20240915-221805@2x.png)

![Image](WX20240915-221821@2x.png)

## The 1-shot Example for Task Demonstration:

## Example Query:

```
Question: Select my preferred language to navigate the Amazon website more comfortably.
```

```
Demonstration example(s) of the task:
Example 1:
Example Question: Choose or update my shipping address to manage where my orders are delivered.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5243
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
