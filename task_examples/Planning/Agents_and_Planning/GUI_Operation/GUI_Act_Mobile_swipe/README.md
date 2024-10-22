# Task: Gui act mobile swipe

## Task Description:

```
Your tasks involves interacting with a smartphone to find information about various topics. Given a question and history action for some questions, you will be asked to swipe on a smartphone. You need to give the correct start and end positions of the swipe. The positions are represented as points in the format of <point>x, y</point>. The position points are normalized to the image size.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](uid_episode_12349968890740372824_step_01.png)

```
Example Question: What's the time in San Francisco?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'Start Point': '<point>0.568, 0.872</point>', 'End Point': '<point>0.422, 0.182</point>'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3534
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning;GUI_Operation
- **Application**: Planning
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Start Point': 'xml_norm_point_distance', 'End Point': 'xml_norm_point_distance'}
  - **Aggregation**: {'function': 'min', 'field_weights': {'Start Point': 1, 'End Point': 1}}
  - **Response Parse Function**: json
- **Source Description**: Data collected from application screenshots by human annotator, and the questions and answers bounding boxes are annotated by human annotator
