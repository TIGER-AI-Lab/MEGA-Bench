# Task: video_detail_description

## Task Description:

```
Please provide a detailed description of the video, focusing on the main subjects, their actions, and the background scenes
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: video_1.mp4]

```
Example Response: Answer: The video starts with a woman cleaning the kitchen sink of a restaurant. She is wearing a black apron over a T-shirt and jeans. The kitchen walls are white-tiled and the kitchen is well-lit. She is cleaning the sink by scooping up the waste in her hand and dumping it in a garbage can behind her. There is a fridge, buckets, and some plates on a metallic shelf beside her. The fridge has a glass door and is full. She closes the dishwasher and washes her hands in the sink. She dries her hand on the apron and walks out of the frame.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 145
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Multimodal_Captioning
- **App**: Perception
- **Input Format**: Videos
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
