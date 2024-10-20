# Task: vln_identify_robot

## Task Description:

```
There are 16 robots working on indoor navigation tasks in parallel, in different rooms. You receive 16 top-down images as the current location for these robots, one for each robot.

Then, you will receive an navigation instruction for one robot.
Your TASK is to identify which robot should execute this navigation instruction by looking at where they are, and assign this instruction to the robot.

Response with "robot i", meaning the robot at i-th image in the image list.
```

![Image](1.png)

![Image](2.png)

![Image](3.png)

![Image](4.png)

![Image](5.png)

![Image](6.png)

![Image](7.png)

![Image](8.png)

![Image](9.png)

![Image](10.png)

![Image](11.png)

![Image](12.png)

![Image](13.png)

![Image](14.png)

![Image](15.png)

![Image](16.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
Example Question: You are facing a potted plant. Turn left and walk straight. Pass through the snooker board an walk straight. Move a step forward and turn right. Pass through the portrait which is left and walk straight. In the right you have stairs. Get down through those stairs. Once you reach the end point of the stairs move a step forward and turn right. Walk straight, there is an open door. Enter into it and walk straight. Turn left and exit the bedroom through the open door. Turn right and move a step forward. You are facing the green plants and you are standing on the walkway. This is the end point.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: robot 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2505
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning;Navigation
- **App**: Planning
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
