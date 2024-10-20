# Task: xor_images

## Task Description:

```
Can you generate a story containing only one of animals from the two images?
```

## The 1-shot Example for Task Demonstration:



## Additional Task Information:

- **ID**: 6164
- **Eval Context**: {'contain_only': '[[fox], [cat, kitten]]'}
- **Taxonomy Tree Path**: Perception;Multimodal_Constrained_Captioning
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##answer': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##answer': 1}}
  - **Response Parse Function**: dummy
