# Task: Xor images

## Task Description:

```
Can you generate a story containing only one of animals from the two images?
```

## The 1-shot Example for Task Demonstration:

## Example Query:

![Image](Figure10.png)

![Image](Figure1.png)



## Additional Information:

- **Sample ID**: 6164
- **Eval Context (for this query sample)**: {'contain_only': '[[fox], [cat, kitten]]'}
- **Taxonomy Tree Path**: Perception;Multimodal_Constrained_Captioning
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##answer': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##answer': 1}}
  - **Response Parse Function**: dummy
- **Source Description**: Images were collected from the Web. Questions and constraints are designed by the annotator. This task has no reference answer
