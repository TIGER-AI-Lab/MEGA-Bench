# Task: vlnqa_egocentric_navigation_video

## Task Description:

```
The task involves analyzing navigation videos where an agent follows a set of instructions. The objective is to determine the next action the agent should take based on the given instructions, such as moving forward, turning left or right, or stopping. The output format should specify the next action as a concise phrase (e.g., Move forward, Turn left and move forward, or Stop).
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 0.mp4]

```
Example Question: This is a navigation video of an agent following the instruction: "Go down the stairs and go into the door on your right. Wait by the toilet." What is the next action it should take?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Turn right and move forward
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 474
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning;Navigation
- **App**: Planning
- **Input Format**: Videos
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
