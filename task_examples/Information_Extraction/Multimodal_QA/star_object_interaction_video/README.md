# Task: Star object interaction video

## Task Description:

```
The task involves identifying objects a person interacts with in various videos based on the provided questions. You need to output the object name.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 0.mp4]

```
Example Question: Which object was taken by the person?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: blanket
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 518
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Multimodal_QA
- **Application**: Information_Extraction
- **Input Format**: Videos
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'multi_ref_phrase'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Videos and annotations were adapted from the STAR benchmark by the human annotator into questions and answers.
