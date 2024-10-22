# Task: Multiview reasoning camera moving

## Task Description:

```
The query images are two frames from a video that shoots a static scene. The first image is from the beginning of the video and the second is from the end of the video. You are asked to answer whether the camera is moving clockwise or counter-clockwise, assuming the movement does not exceed 180 degrees. The answer should be from ('clockwise', 'counter-clockwise').
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](test_Multi-view_Reasoning_1_1.png)

![Image](test_Multi-view_Reasoning_1_2.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 'counter-clockwise'
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 2745
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;3D_understanding
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were collected from BLINK. Questions and answers were re-designed and augmented by the annotator
