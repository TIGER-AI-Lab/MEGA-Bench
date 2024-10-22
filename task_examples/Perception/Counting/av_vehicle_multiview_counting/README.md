# Task: Av vehicle multiview counting

## Task Description:

```
The six multi-view images are captured from cameras mounted on an autonomous-driving vehicle. The six cameras are placed at the vehicle's back, back-left, back-right, front, front-left, and front-right. Six images from the six cameras are presented in order, and bounding boxes are plotted to indicate the instances you should consider. Your task is to count the number of unique vehicles (car, bicycle, truck) in the scene based on those bounding boxes. Make sure to do proper 3d reasoning and do not count the same instance multiple times.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0_CAM_BACK.png)

![Image](0_CAM_BACK_LEFT.png)

![Image](0_CAM_BACK_RIGHT.png)

![Image](0_CAM_FRONT.png)

![Image](0_CAM_FRONT_LEFT.png)

![Image](0_CAM_FRONT_RIGHT.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 5
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1799
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Counting
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'vehicles': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'vehicles': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were collected from the nuScenes dataset. The annotator designed the questions and implemented a script to generate the answers from the raw annotation
