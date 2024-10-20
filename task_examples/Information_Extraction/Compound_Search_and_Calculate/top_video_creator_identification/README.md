# Task: top_video_creator_identification

## Task Description:

```
Determine the creator of the video with the highest number of views on a YouTube page based on a screenshot.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](top_video_creator_identification1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: MrBeast
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3140
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Compound_Search_and_Calculate
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'creator': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'creator': 1}}
  - **Response Parse Function**: answer_string
