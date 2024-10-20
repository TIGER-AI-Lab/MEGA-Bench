# Task: contain_contain_images

## Task Description:

```
Can you write a story containing the both of the animals appearing in the individual images?
```

## The 1-shot Example for Task Demonstration:



## Additional Task Information:

- **ID**: 6254
- **Eval Context**: {'contain1': '[cat, kitten]', 'contain2': '[dog, puppy, pup]'}
- **Taxonomy Tree Path**: Perception;Multimodal_Constrained_Captioning
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##answer': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##answer': 1}}
  - **Response Parse Function**: dummy
