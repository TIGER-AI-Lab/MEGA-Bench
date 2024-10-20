# Task: multilingual_movie_info_parsing

## Task Description:

```
Given a screenshot of a multilingual movie information page, extract the following information with the corresponding language:

(1) Movie Title
(2) Number of Star
(3) Number of Ratings
(4) IMDb score
(5) Duration of the Movie
(6) Release Year
(7) Movie Genres

If any of the above information is not present in the image, leave it blank.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](multilingual_movie_info_parsing1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'title': 'JACKPOT!', 'star': '3.5', 'rating': '272', 'score': '5.8', 'duration': '1 h 46 min', 'year': '2024', 'genres': 'Comedy, Action'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1707
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Structured_Parsing
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'title': 'simple_str_match', 'star': 'simple_str_match', 'rating': 'simple_str_match', 'score': 'simple_str_match', 'duration': 'simple_str_match', 'year': 'simple_str_match', 'genres': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'title': 1, 'star': 1, 'rating': 1, 'score': 1, 'duration': 1, 'year': 1, 'genres': 1}}
  - **Response Parse Function**: json
