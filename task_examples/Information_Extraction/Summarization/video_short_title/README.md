# Task: Video short title

## Task Description:

```
You are a multi-modal AI assistant. You are given a short video, please generate a short, concise but attractive title for the video.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 1.mp4]

```
Example Response: Answer: "Mastering Split Screen in Windows 10: A Quick Guide"
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Information:

- **Sample ID**: 275
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Summarization
- **Application**: Information_Extraction
- **Input Format**: Videos
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Videos taken from [YouTube](https://www.youtube.com/). Questions and answers created by human annnotator.
