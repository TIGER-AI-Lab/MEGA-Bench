# Task: perception_test_object_shuffle_video

## Task Description:

```
The task involves watching videos where a person plays an occlusion game with multiple similar objects. The goal is to identify the position of the hidden object at the end of the game from the person's point of view, with the position counted from the left. The answer is provided as the object's position (e.g., first, second, third, etc.).
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 0.mp4]

```
Example Question: The person uses multiple similar objects to play an occlusion game. Where is the hidden object at the end of the game from the person's point of view?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: third
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 718
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games
- **App**: Planning
- **Input Format**: Videos
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
