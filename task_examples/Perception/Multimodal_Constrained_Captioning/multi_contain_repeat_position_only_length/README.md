# Task: multi_contain_repeat_position_only_length

## Task Description:



## The 1-shot Example for Task Demonstration:



## Additional Task Information:

- **ID**: 6239
- **Eval Context**: {'contain1##times': '[robot]##3', 'contain2##position_only': '[car, vehicle]##1', 'length1': '>50', 'length2': '<200'}
- **Taxonomy Tree Path**: Perception;Multimodal_Constrained_Captioning
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##output': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##output': 1}}
  - **Response Parse Function**: dummy
