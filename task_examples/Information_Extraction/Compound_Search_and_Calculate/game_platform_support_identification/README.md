# Task: Game platform support identification

## Task Description:

```
Give a screenshot of a game description page from the Steam store website. (1) Determine and identify the supported platforms (Windows, MacOS, SteamOS or Linux), separated by commas. (2) Count the number of supported platforms.

Use the capitalization specified in the prompt above, not the one in the image. Treat SteamOS and Linux as separate platforms.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](game_platform_support_identification_1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'supported platforms': 'Windows', 'number': '1'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3520
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Compound_Search_and_Calculate
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'supported platforms': 'set_equality', 'number': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'supported platforms': 1, 'number': 1}}
  - **Response Parse Function**: json
- **Source Description**: Screenshots were taken by the human annotator on the [Steam store](https://store.steampowered.com/). Questions and answers were created by the annotator.
