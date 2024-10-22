# Task: App layout understanding ppt

## Task Description:

```
The image below is a screenshot of the Microsoft PowerPoint app. From the options listed, identify the function highlighted by the red box in the picture: [Change font, Adjust font size, Select shape, Add notes, Quickly insert a text box, Select an image, Fill with current orange color, Choose fill color, Outline with current blue color, Select outline color, "I want to add an animation to the slides", "I want to add a comment for my collaborator", "I want to move the title a bit to the right", "I want to use AI to assist me in designing slides", "I want to record a video to teach my students how to create slides"].
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](WX20240803-131835@2x.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Change font
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5922
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;App_Function_Understanding
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Screenshots were taken by the human annotator on Microsoft PowerPoint. Questions and answers were created by the annotator.
