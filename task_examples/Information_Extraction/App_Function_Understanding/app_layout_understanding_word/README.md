# Task: App layout understanding word

## Task Description:

```
The images below are screenshots of the Microsoft Word application interface. From the following list of features, identify the function indicated by the red boxes in the images: [Save, Print, Insert, Bullet Points, Center Align, Right Align, Change Font, Change Font Size, Bold Font, Adjust Layout, "I want to insert a table but I don't know how to do it", "I want to view my document in web layout", "I want to manage this document in Zotero", "Format painter", "I want to set up auto-save"]
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](WX20240801-232834@2x.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Save
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5880
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;App_Function_Understanding
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Screenshots were taken by the human annotator on Microsoft Word. Questions and answers were created by the annotator.
