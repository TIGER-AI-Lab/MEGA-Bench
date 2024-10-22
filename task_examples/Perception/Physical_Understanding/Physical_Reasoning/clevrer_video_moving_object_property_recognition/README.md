# Task: Clevrer video moving object property recognition

## Task Description:

```
The task involves identifying objects' color, shape, material, and motion status at specific points in a video. You need topurple answer the question based on the given video.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 0.mp4]

```
Example Question: What color is the object that is stationary?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: gray
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1152
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Physical_Understanding;Physical_Reasoning
- **Application**: Perception
- **Input Format**: Videos
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'multi_ref_phrase'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: The videos are collected from MVBench, the questions and answers are adapted to test the understanding of physical property and dynamics
