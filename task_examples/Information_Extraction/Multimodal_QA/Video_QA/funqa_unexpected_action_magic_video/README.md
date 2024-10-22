# Task: Funqa unexpected action magic video

## Task Description:

```
The task involves analyzing videos to identify surprising or magical actions and elements, focusing on illusions, unexpected reveals, or fantastical transitions. The objective is to describe the magical or surprising event in the video with accuracy and detail.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 0.mp4]

```
Example Question: What surprising event occurs when the book is opened inside the library?
Example Response: Answer: A large black hole is revealed behind a shifting bookshelf.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Information:

- **Sample ID**: 619
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
