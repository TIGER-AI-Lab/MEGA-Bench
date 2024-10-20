# Task: video_qa

## Task Description:

```
You are a multi-modal AI assistant. You are given a short video, please watch it and then answer the following question.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 1.mp4]

```
Example Question: What are the steps to create a three-window split screen setup in Windows 10, and how can you expand it to a four-window layout?
Example Response: Answer: To create a three-window split screen setup in Windows 10, follow these steps:

1. Start by dragging one window to a corner of the screen. This will snap it into place, occupying approximately one-quarter of the screen.

2. Take a second window and drag it to fill the space directly below the first window. This will create two vertically stacked windows on one side of the screen.

3. The remaining space on the opposite side of the screen will display options for active windows. Select one of these to fill the larger third window space.

This setup creates a layout with two smaller windows on one side and a larger window on the other side.

To expand this to a four-window layout:

4. Drag the larger window on the side with one window into a corner. This action will resize it to match the other corner windows.

5. The system will then display options for active windows to fill the newly created fourth space. Select a window to complete the four-window layout.

It's important to note that this feature works best on larger monitors, as it allows for more comfortable viewing and interaction with multiple windows simultaneously. The Windows 10 operating system automatically adjusts the size and position of the windows to fit the screen optimally.

Additionally, you can use keyboard shortcuts to streamline this process. The Windows key + arrow keys can quickly snap windows to different parts of the screen, making it easier to arrange multiple windows without relying solely on mouse dragging.

Remember that you can always readjust the size of the windows by dragging the borders between them, allowing for further customization of your split-screen setup to suit your specific needs and preferences.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 74
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Multimodal_QA;Video_QA
- **App**: Information_Extraction
- **Input Format**: Videos
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
