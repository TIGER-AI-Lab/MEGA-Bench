# Task: App interactive operations instagram

## Task Description:

```
The ten images below each feature a red box highlighting different function buttons on the Instagram interface. Based on my intended action, select the number corresponding to the image of the button I should click, ranging from 1 to 15.
```

![Image](WX20240803-133450@2x.png)

![Image](WX20240803-133506@2x.png)

![Image](WX20240803-133521@2x.png)

![Image](WX20240803-133708@2x.png)

![Image](WX20240803-133724@2x.png)

![Image](WX20240803-133738@2x.png)

![Image](WX20240803-133835@2x.png)

![Image](WX20240803-133916@2x.png)

![Image](WX20240803-133942@2x.png)

![Image](WX20240803-134039@2x.png)

![Image](WX20240902-174701@2x.png)

![Image](WX20240902-174828@2x.png)

![Image](WX20240902-174842@2x.png)

![Image](WX20240902-174901@2x.png)

![Image](WX20240902-175139@2x.png)

## The 1-shot Example for Task Demonstration:

## Example Query:

```
Question: Use the 'Comment' feature to add my thoughts or reactions to a post.
```

```
Demonstration example(s) of the task:
Example 1:
Example Question: Tap the 'Like' button to express appreciation for a post
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5387
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
