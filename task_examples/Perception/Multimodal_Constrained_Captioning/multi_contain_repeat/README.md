# Task: Multi contain repeat

## Task Description:

```
Please follow the instructions to write a story.
```

## The 1-shot Example for Task Demonstration:

## Example Query:

![Image](10-robot.png)

![Image](3-car.png)

```
Question: Please write a story using the concepts/entities in the two images. The first image's concept should appear 3 times, and the second image's concept should only appear once. The appearance times should be accurate, generating more or less will be considered as wrong.
```



## Additional Information:

- **Sample ID**: 6224
- **Eval Context (for this query sample)**: {'contain1##times': '[robot]##3', 'contain2##times': '[car, vehicle]##1', 'contain3##times': ''}
- **Taxonomy Tree Path**: Perception;Multimodal_Constrained_Captioning
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##output': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##output': 1}}
  - **Response Parse Function**: dummy
- **Source Description**: Images were collected from the Web. Questions and constraints are designed by the annotator. This task has no reference answer
