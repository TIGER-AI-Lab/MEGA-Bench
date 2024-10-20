# Task: youtube_video_info_parsing

## Task Description:

```
Given a screenshot from Youtube, parse the information for the following questions: (1) Video title (2) Publisher's name (3) Number of likes (4) Number of comments (5) Number of views within a certain time frame. (6) Number of subscribers

Numbers should not include any commas every three digits. When reporting the number of views and age of the video, do not include the words "views" or "ago".
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](youtube_video_info_parsing1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'title': 'ABC World News Tonight with David Muir Full Broadcast - Aug. 6, 2024', 'name': 'ABC News', 'likes': '3.7K', 'comments': '840', 'views': '265066, 6 hours', 'subscribers': '17.1M'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 131
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Structured_Parsing
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'title': 'simple_str_match', 'name': 'simple_str_match', 'likes': 'simple_str_match', 'comments': 'simple_str_match', 'views': 'simple_str_match', 'subscribers': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'title': 1, 'name': 1, 'likes': 1, 'comments': 1, 'views': 1, 'subscribers': 1}}
  - **Response Parse Function**: json
