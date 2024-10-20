# Task: nextqa_mc

## Task Description:

```
Watch the given video and answer the question. Answer with the letter corresponding to the correct option.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: video_1.mp4]

```
Example Question: what animal was shown in the video

Options:
A: snake
B: dogs
C: elephants
D: squirrel
E: swans
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: A
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1339
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Multimodal_QA;Video_QA
- **App**: Information_Extraction
- **Input Format**: Videos
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
