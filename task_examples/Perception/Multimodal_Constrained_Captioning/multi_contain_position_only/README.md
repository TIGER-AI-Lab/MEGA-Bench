# Task: Multi contain position only

## Task Description:

```
Please follow the instructions to write a story.
```

## The 1-shot Example for Task Demonstration:

## Example Query:

![Image](1.png)

![Image](6_polar_bear.png)

```
Question: Please write a story using the two concepts shown in the two images. The first image's concept only appears in the first sentence, and the second image's concept only appears in the third sentence.
```



## Additional Information:

- **Sample ID**: 6149
- **Eval Context (for this query sample)**: {'contain1##position_only': '[forest]##1', 'contain2##position_only': '[polar bear, white bear, ice bear]##3', 'contain3##position_only': ''}
- **Taxonomy Tree Path**: Perception;Multimodal_Constrained_Captioning
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##output': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##output': 1}}
  - **Response Parse Function**: dummy
- **Source Description**: Images were collected from the Web. Questions and constraints are designed by the annotator. This task has no reference answer
