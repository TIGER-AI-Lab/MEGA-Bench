# Task: multi_contain_position_only

## Task Description:

```
Please follow the instructions to write a story.
```

## The 1-shot Example for Task Demonstration:



## Additional Task Information:

- **ID**: 6149
- **Eval Context**: {'contain1##position_only': '[forest]##1', 'contain2##position_only': '[polar bear, white bear, ice bear]##3', 'contain3##position_only': ''}
- **Taxonomy Tree Path**: Perception;Multimodal_Constrained_Captioning
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##output': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##output': 1}}
  - **Response Parse Function**: dummy
