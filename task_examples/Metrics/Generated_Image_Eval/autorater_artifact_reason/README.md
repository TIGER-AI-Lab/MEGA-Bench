# Task: autorater_artifact_reason

## Task Description:

```
Please tell me why this image contains artifacts? Please answer with the following format "The [subject] is [reason]". Please fill out [subject] and [reason], and [subject] is an entity in the image.
```

## The 1-shot Example for Task Demonstration:



## Additional Task Information:

- **ID**: 5681
- **Eval Context**: {'contain1': '[beer, glass]', 'contain2': '[is, are]'}
- **Taxonomy Tree Path**: Metrics;Generated_Image_Eval
- **App**: Metrics
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##answer': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##answer': 1}}
  - **Response Parse Function**: dummy
