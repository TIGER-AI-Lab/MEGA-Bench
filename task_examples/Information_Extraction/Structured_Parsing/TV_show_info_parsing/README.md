# Task: Tv show info parsing

## Task Description:

```
Given a screenshot of a TV show information page, extract the following information:

(1) TV Show Title
(2) Season Number
(3) Number of Star
(4) Number of Ratings
(5) IMDb Score
(6) Release Year
(7) Number of Episodes
(8) Available Formats (e.g. X-RAY, HDR, UHD, Subtitle, AD)
(9) TV Show Genres

If any of the above information is not present in the image, leave it blank. For number outputs, please omit any commas.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](TV_show_info_parsing1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'title': 'Mirzapur', 'season': '3', 'star': '3.5', 'rating': '32', 'score': '8.5', 'year': '2024', 'episodes': '10', 'format': 'X-RAY, UHD, 18+, Subtitle, AD', 'genres': 'Action, Drama, Suspense'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 365
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Structured_Parsing
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'title': 'simple_str_match', 'season': 'simple_str_match', 'star': 'simple_str_match', 'rating': 'simple_str_match', 'score': 'simple_str_match', 'year': 'simple_str_match', 'episodes': 'simple_str_match', 'format': 'simple_str_match', 'genres': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'title': 1, 'season': 1, 'star': 1, 'rating': 1, 'score': 1, 'year': 1, 'episodes': 1, 'format': 1, 'genres': 1}}
  - **Response Parse Function**: json
- **Source Description**: Screenshots were taken by the human annotator on the [Amazon Prime Video webpage](https://www.primevideo.com/). Questions and answers were created by the annotator.
