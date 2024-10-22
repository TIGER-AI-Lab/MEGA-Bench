# Task: Funqa unexpected action creative video

## Task Description:

```
This task involves analyzing videos to identify and describe surprising or creative actions. These actions range from humorous events to unique performances, where the unexpected or inventive element is key. The goal is to explain what makes the video surprising or creatively engaging based on the actions depicted.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 0.mp4]

```
Example Question: What is the unexpected material used for the racecar in the video?
Example Response: Answer: Fabricated from paper.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Information:

- **Sample ID**: 202
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Multimodal_QA;Video_QA
- **Application**: Information_Extraction
- **Input Format**: Videos
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Videos and annotations were adapted from the FunQA benchmark by the human annotator into being an open-ended question.
