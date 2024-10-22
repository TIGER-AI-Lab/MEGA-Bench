# Task: Contain length

## Task Description:



## The 1-shot Example for Task Demonstration:

## Example Query:

![Image](Figure1.png)

```
Question: Can you write a story about the animal in the figure with more than 10 but less than 20 words?
```



## Additional Information:

- **Sample ID**: 6269
- **Eval Context (for this query sample)**: {'contain': '[cat, kitten]', 'length1': '>10', 'length2': '<20'}
- **Taxonomy Tree Path**: Perception;Multimodal_Constrained_Captioning
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'##answer': 'constrained_generation'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'##answer': 1}}
  - **Response Parse Function**: dummy
- **Source Description**: Images were collected from the Web. Questions and constraints are designed by the annotator. This task has no reference answer
