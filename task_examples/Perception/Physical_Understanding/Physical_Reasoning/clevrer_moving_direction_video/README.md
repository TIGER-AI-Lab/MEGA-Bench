# Task: Clevrer moving direction video

## Task Description:

```
The task involves identifying the direction of movement of various objects, such as spheres and cylinders, within videos. The objects may be stationary or move in specific directions, and the direction is described using terms like up, down, left, and right, or combinations of these. The answers are provided in the format of movement directions or as stationary if the object is not moving. The output should be one or two words
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 1.mp4]

```
Example Question: What direction is the gray cylinder moving in within the video?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: down right
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 819
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Physical_Understanding;Physical_Reasoning
- **Application**: Perception
- **Input Format**: Videos
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'multi_ref_phrase'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Video data are collected from MVBench. Questions and answers are adapted for the contextual formatted output format
