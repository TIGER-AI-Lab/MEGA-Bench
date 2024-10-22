# Task: App layout understanding youtube

## Task Description:

```
The images below are screenshots of the YouTube app interface. From the following functionalities, identify the one indicated by the red box in each image: [Like, Dislike, Comment, Save, Pause Video, Exit Full Screen, Skip to Previous Video, Skip to Next Video, Turn on Subtitles, Open Settings, Set whether to enable autoplay, I'm interested in videos about Mr. Bean, Cast the screen to the projector in my living room, View the text description of this video, This video is too slow-paced, I want to fast-forward directly to the interesting content].
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](WX20240801-215221@2x.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Like
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5795
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;App_Function_Understanding
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Screenshots were taken by the human annotator on [YouTube](https://www.youtube.com/). Questions and answers were created by the annotator.
