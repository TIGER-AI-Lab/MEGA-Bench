# Task: App layout understanding tiktok

## Task Description:

```
The image below is a screenshot of the TikTok interface. From the following options, identify the feature highlighted by the red box in the image: [Like, Comment, Bookmark, Share, Follow, View Vlogger's Homepage, Watch Live Stream, View the Location of this Video, View the Background Music Used in this Video, Post a TikTok Video, "I want to see today's trending searches", "I want to watch short videos posted by people I follow", "I want to check who has sent me direct messages", "This song sounds pretty good", "Edit my profile"].
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](WX20240802-214811@2x.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Like
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5809
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;App_Function_Understanding
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Screenshots were taken by the human annotator on the TikTok app. Questions and answers were created by the annotator.
