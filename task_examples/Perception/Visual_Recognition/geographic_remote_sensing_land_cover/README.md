# Task: geographic_remote_sensing_land_cover

## Task Description:

```
Your task is to recognize the land cover, specifically the biophysical surface characteristics, of the given satellite images. For each test case, there are two images. There are 10 possible choices: ['beach', 'circular farmland', 'cloud', 'desert', 'forest', 'mountain', 'rectangular farmland', 'residential', 'river', 'snowberg'].
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1_beach.png)

![Image](1_forest.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: beach, forest
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4677
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Visual_Recognition
- **App**: Perception
- **Input Format**: 3D Models and Aerial Imagery
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'sequence_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
