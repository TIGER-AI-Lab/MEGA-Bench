# Task: 3d_indoor_scene_text_bbox_selection

## Task Description:

```
This task asks you to select the correct 2D bounding box from a set of predefined candidates in a 3D indoor scene based on a text query. Each bounding box is labeled with a unique number on the middle top (from 1 to 15). The text query describes an object with details. Please identify which of the numbered bounding boxes corresponds to the described entity. Answer the bounding box index only.
```

![Image](scene_with_bbox.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
Example Question: It is a wooden barstool. It sits behind the bar, and is the second one in from the edge of the bar. The most left one.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 10
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 897
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;3D_understanding
- **App**: Perception
- **Input Format**: 3D Models and Aerial Imagery
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'bbox number': 'exact_str_match', '': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'bbox number': 1, '': 1}}
  - **Response Parse Function**: answer_string
