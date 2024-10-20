# Task: song_title_identification_from_lyrics

## Task Description:

```
Given a screenshot of lyrics from an online music streaming website, infer the following information: (1) The title of the song (2) The name of the artist.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](song_title_identification_from_lyrics1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'title': 'Rhythm of the Rain', 'name': 'The Cascades'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2229
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge
- **App**: Knowledge
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'title': 'exact_str_match', 'name': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'title': 1, 'name': 1}}
  - **Response Parse Function**: json
