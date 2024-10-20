# Task: video2notes

## Task Description:

```
You are a multi-modal AI assistant. You are given a short video, please watch it and generate a structured class note for the video.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 1.mp4]

```
Example Response: Answer: 
# Note on Using Split Screen on Windows 10

## Chapter 1: Intro

Overview of split screen functionality in Windows 10.

The video covers various window-snapping variations.

Clickable links are provided for easy navigation to different options.

## Chapter 2: Two-Window Screen

Introduction to two-window screen setup.

Windows 10 enhances window-snapping features from previous OS versions.

### Steps to Snap Windows:

1. Click and hold the title bar of the window.
2. Drag it to the left or right edge of the screen until the mouse cursor disappears.
3. Release the cursor when the window flashes an outline.
4. The window is now pinned to that half of the screen.

### Active Windows Display:

A collection of other active windows will appear on the opposite side.

Click on any active window to snap it into the other half of the screen.

### Keyboard Shortcut:

Use the Windows key + arrow key (left or right) to quickly snap the active window to either side of the screen.

Repeat the process with another window on the opposite side or select from the options that appear.

## Chapter 3: Three-or-Four-Window Screen

Expanding to three or four snapped windows on larger monitors.

### Steps for Three Windows:

1. Drag a window to a corner of the screen to snap it there.
2. Take another window and drag it to fill the space below the first window.

### Filling Remaining Space:

The left side will show options to fill the remaining slot with a larger third window.

### Adding a Fourth Window:

Drag the left window into a corner to create a fourth window.

Fill the final space with the fourth window.

Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 378
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Summarization
- **App**: Information_Extraction
- **Input Format**: Videos
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
