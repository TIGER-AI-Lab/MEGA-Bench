# Task: Widerface face count and event classification

## Task Description:

```
Given a query image, count the number of faces in the image and also tell the event. Candidate events include: Concerts,  Dresses, Cheering, Election campaign, Marching, Demonstration, Drilling, Soccer, Hockey, Press conference, Picnic, Riot, Car Accident, Funeral, Gymnastics. Note that completely occuluded or invisible faces are not counted.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](e1_9_Press_Conference_Press_Conference_9_60.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'Number of faces': '7', 'Event': 'Press conference'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 205
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Visual_Recognition
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Number of faces': 'exact_str_match', 'Event': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Number of faces': 1, 'Event': 1}}
  - **Response Parse Function**: json
- **Source Description**: Images were collected from WiderFace. Questions and answers were designed and produced by the annotator
