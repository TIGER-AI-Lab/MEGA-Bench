# Task: Video segments reordering

## Task Description:

```
Given the first video frame and shuffled remaining video frames that are extracted from video, please reorder the video frames as the time goes based on the given first frame. The index of first video frame is 1. The answer should be list including the index of 1 and the remaining image indexs following the given first frame in order.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](Bowling0001.png)

![Image](Bowling0002.png)

![Image](Bowling0004.png)

![Image](Bowling0005.png)

![Image](Bowling0003.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: [1, 2, 5, 3, 4]
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3946
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Temporal_Understanding
- **Application**: Perception
- **Input Format**: Videos
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'sequence_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Raw data come from UCF101. The annotator designed the task and re-organized the data to produce the question-answer pairs
