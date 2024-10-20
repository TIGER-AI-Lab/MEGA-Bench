# Task: video_summary

## Task Description:

```
You are a multi-modal AI assistant. You are given a video, please summarize the video in one short paragraph. Your goal is to provide a comprehensive, informative but concise summary based on the video content.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 1.mp4]

```
Example Response: Answer: This video provides a comprehensive guide on using split screen functionality in Windows 10. It covers two-window, three-window, and four-window setups. The video explains the process of snapping windows to different parts of the screen using both mouse dragging techniques and keyboard shortcuts. For two-window setups, users can drag windows to the left or right edges of the screen or use the Windows key + arrow key shortcut. For three or four windows, the process involves dragging windows to screen corners. The guide also mentions that Windows 10 enhances window-snapping features from previous OS versions and provides options for filling remaining screen space with active windows.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 447
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Summarization
- **App**: Information_Extraction
- **Input Format**: Videos
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
