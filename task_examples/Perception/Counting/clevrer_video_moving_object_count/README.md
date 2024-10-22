# Task: Clevrer video moving object count

## Task Description:

```
Given a video of video and static objects, answer the corresponding questions. The output should be a number.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 0.mp4]

```
Example Question: How many red objects are moving?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 2
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 248
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Counting
- **Application**: Perception
- **Input Format**: Videos
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Video data are collected from MVBench. Questions and answers are adapted for the direct numerical output
