# Task: Video grounding spatial

## Task Description:

```
Given a video and some sentences below, choose where the characers or objects or actions or scenes described in the sentences appears in the video. Specifically, imagine that we divide the video into several segments (segment-1, segment-2, segment-3, ...) evenly, then we specify one segment (like segment-2) and ask where the characers or objects or actions or scenes described in the sentences appear in the video (like Upper 1/3, Bottom 1/3, Left 1/3 and so on, the options will be specified in the question).
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 1.mp4]

```
Example Question: Suppose the video is divided into 10 segments, every sgement is 4 seconds. In segment-1, When did a black dog first appear? Choose from {upper left corner, upper right corner, lower left corner, lower right corner, directly top, directly bottom, directly left, directly right, center}
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: upper right corner
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3431
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Spatial_Understanding
- **Application**: Perception
- **Input Format**: Videos
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Videos collected from VidOR. Re-designed questions and answers for this specific task
