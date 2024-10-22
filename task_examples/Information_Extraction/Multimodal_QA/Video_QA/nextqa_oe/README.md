# Task: Nextqa oe

## Task Description:

```
Watch the given video and answer the question.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: video_1.mp4]

```
Example Question: what activity is being carried out (answer should be a one-word verb)
Example Response: Answer: skiing
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Information:

- **Sample ID**: 518
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Multimodal_QA;Video_QA
- **Application**: Information_Extraction
- **Input Format**: Videos
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'answer': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images and annotations were adapted from the NExTQA benchmark by the human annotator into being an open-ended question.
