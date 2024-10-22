# Task: App layout understanding excel

## Task Description:

```
The image below is a screenshot of the Microsoft Word interface. From the options listed, identify the function highlighted by the red box in the picture: [Change font, Adjust font size, Filter by the value of EVALUATION, Create a new sheet, Enter insert interface, Select Column E, Select Row 9, Align left, Zoom in, Merge cells and center, "I want to display all the text in an Excel cell without adjusting the cell width, that is, to wrap the text automatically", "I want to find the cell containing 'is there a fracture'", "I want to edit a formula", "Format painter", "I want to adjust the border display of the table to make my table clearer"].
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](WX20240803-150755@2x.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Change font
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5823
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;App_Function_Understanding
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Screenshots were taken by the human annotator on Microsoft Excel. Questions and answers were created by the annotator.
