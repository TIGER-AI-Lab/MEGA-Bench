# Task: funqa_unexpected_action_humor_video

## Task Description:

```
This task involves analyzing videos to identify and describe humorous or unexpected actions. The objective is to capture the event or twist that makes the video amusing or surprising. The focus is on identifying the key actions or elements that contribute to the humor or unexpected outcome in the video.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 0.mp4]

```
Example Question: What surprising action did the dog do to the snake in the video?
Example Response: Answer: The dog pulled the snake towards itself, making it jump.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 30
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Multimodal_QA;Video_QA
- **App**: Information_Extraction
- **Input Format**: Videos
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
