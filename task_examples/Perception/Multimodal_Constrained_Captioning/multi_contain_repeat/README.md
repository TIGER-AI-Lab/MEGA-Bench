# Task: multi_contain_repeat

## Task Description:

```
Please follow the instructions to write a story.
```

## The 1-shot Example for Task Demonstration:



## Additional Task Information:

- **ID**: 6224
- **Eval Context**: {'contain1##times': '[robot]##3', 'contain2##times': '[car, vehicle]##1', 'contain3##times': ''}
- **Taxonomy Tree Path**: Perception;Multimodal_Constrained_Captioning
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##output': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##output': 1}}
  - **Response Parse Function**: dummy
