# Task: App layout understanding notes

## Task Description:

```
The image below is a screenshot of the Notes app on an iPhone. From the options listed, identify the function highlighted by the red box in the picture: [I made a mistake, undo; Send my note to my roommate; This note is finished, ready to write the next one; I want to add my employment contract to it; there are five things to do today, I want to record them in the note; Let's use the note for today's market bill, I bought seven items in total, record the name and unit price for each; I want to write in Chinese; I'm in a good mood today, let's add a smiley face; This math problem is a bit difficult today, I'll sketch a rough diagram first to record my thoughts; I wrote it wrong, delete this word; Set all attachment view to small; Use capital letters to record a title, it will be more eye-catching this way; I made a mistake undoing, undo again to go back; Set left and right alignment; I want to go outside to view attachments].
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](WX20240803-132400@2x.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: I made a mistake, undo
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5767
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;App_Function_Understanding
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Screenshots were taken by the human annotator on the Google Notes app. Questions and answers were created by the annotator.
