# Task: contain_length

## Task Description:



## The 1-shot Example for Task Demonstration:



## Additional Task Information:

- **ID**: 6269
- **Eval Context**: {'contain': '[cat, kitten]', 'length1': '>10', 'length2': '<20'}
- **Taxonomy Tree Path**: Perception;Multimodal_Constrained_Captioning
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##answer': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##answer': 1}}
  - **Response Parse Function**: dummy
