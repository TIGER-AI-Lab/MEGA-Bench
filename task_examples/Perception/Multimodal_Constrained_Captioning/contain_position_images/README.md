# Task: contain_position_images

## Task Description:



## The 1-shot Example for Task Demonstration:



## Additional Task Information:

- **ID**: 6209
- **Eval Context**: {'contain1##position': '[elephant]##2', 'contain2##position': '[parrot]##2'}
- **Taxonomy Tree Path**: Perception;Multimodal_Constrained_Captioning
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##answer': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##answer': 1}}
  - **Response Parse Function**: dummy
