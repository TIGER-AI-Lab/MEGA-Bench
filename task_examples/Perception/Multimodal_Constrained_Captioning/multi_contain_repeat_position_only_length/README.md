# Task: Multi contain repeat position only length

## Task Description:



## The 1-shot Example for Task Demonstration:

## Example Query:

![Image](10-robot.png)

![Image](3-car.png)

```
Question: Please write a story using the concepts/entities in the two images. The story should have more than 50 but less than 200 words. The first image's concept should appear 3 times, and the second image's concept should only appear in the first sentence. The appearance times and location should be accurate, generating more or less will be considered as wrong.
```



## Additional Information:

- **Sample ID**: 6239
- **Eval Context (for this query sample)**: {'contain1##times': '[robot]##3', 'contain2##position_only': '[car, vehicle]##1', 'length1': '>50', 'length2': '<200'}
- **Taxonomy Tree Path**: Perception;Multimodal_Constrained_Captioning
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##output': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##output': 1}}
  - **Response Parse Function**: dummy
- **Source Description**: Images were collected from the Web. Questions and constraints are designed by the annotator. This task has no reference answer
