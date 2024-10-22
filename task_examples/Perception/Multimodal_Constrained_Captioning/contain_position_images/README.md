# Task: Contain position images

## Task Description:



## The 1-shot Example for Task Demonstration:

## Example Query:

![Image](Figure3.png)

![Image](Figure4.png)

```
Question: Write a story containing both of the animals in the two images. They need to both appear in the second sentence.
```



## Additional Information:

- **Sample ID**: 6209
- **Eval Context (for this query sample)**: {'contain1##position': '[elephant]##2', 'contain2##position': '[parrot]##2'}
- **Taxonomy Tree Path**: Perception;Multimodal_Constrained_Captioning
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##answer': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##answer': 1}}
  - **Response Parse Function**: dummy
- **Source Description**: Images were collected from the Web. Questions and constraints are designed by the annotator. This task has no reference answer
