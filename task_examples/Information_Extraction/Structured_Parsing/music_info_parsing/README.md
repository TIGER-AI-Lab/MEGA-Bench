# Task: Music info parsing

## Task Description:

```
Given a screenshot of an online music webpage, extract the following information:

(1) Song title
(2) Total song duration
(3) Recent play time
(4) Main artist
(5) Composer
(6) Lyricist
(7) Producer
(8) Third line of the lyrics

If any of the above information is not present in the image, leave it blank.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](music_info_parsing1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'title': '...Baby One More Time', 'duration': '3:31', 'recent_time': '0:21', 'artist': 'Britney Spears', 'composer': 'Max Martin', 'lyricist': 'Max Martin', 'producer': 'Max Martin, Rami Yacoub', 'lyrics_3': 'Oh, baby, baby, how was I supposed to know'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1684
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Structured_Parsing
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'title': 'simple_str_match', 'duration': 'simple_str_match', 'recent_time': 'simple_str_match', 'artist': 'simple_str_match', 'composer': 'simple_str_match', 'lyricist': 'simple_str_match', 'producer': 'simple_str_match', 'lyrics_3': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'title': 1, 'duration': 1, 'recent_time': 1, 'artist': 1, 'composer': 1, 'lyricist': 1, 'producer': 1, 'lyrics_3': 1}}
  - **Response Parse Function**: json
- **Source Description**: Screenshots were taken by the human annotator on the [Spotify Web Player](https://open.spotify.com/). Questions and answers were created by the annotator.
