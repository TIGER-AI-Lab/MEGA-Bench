# Task: App layout understanding instagram

## Task Description:

```
The image below is a screenshot of the Instagram interface. From the options listed, identify the function highlighted by the red box in the picture: [Like, Comment, Share, Save, Turn off mute, Post a new post, Go to profile, Enter short video mode, Refresh or return to homepage, Search, The comment section is interesting, I want to see more fun comments, I want to view the content posted by the people I follow, find friends to follow and message, Check new messages and notifications, I want to see more information about this video].
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](WX20240803-133450@2x.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Like
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5851
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;App_Function_Understanding
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Screenshots were taken by the human annotator on the Instagram app. Questions and answers were created by the annotator.
