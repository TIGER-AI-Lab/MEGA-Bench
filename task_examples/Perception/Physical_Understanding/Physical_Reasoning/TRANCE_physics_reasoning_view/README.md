# Task: TRANCE_physics_reasoning_view

## Task Description:

```
You will be given 2 images, the start and end state of a system respectively. You will be given a list of items, with their index, size, color, material, shape and position. You should answer the question based on the given information. Note that not all the objects in the list is shown in the picture, and the camera position in different pictures may be different.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](10.png)

![Image](11.png)

```
Example Question: | obj | size   | color | material | shape    | position |
|-----|--------|-------|----------|----------|----------|
| 0   | small  | red   | rubber   | cube     | 16,-20   |
| 1   | medium | red   | rubber   | cylinder | -6,17    |
| 2   | small  | green | glass    | sphere   | 2,19     |
| 3   | small  | gray  | rubber   | cube     | 24,23    |
| 4   | large  | blue  | rubber   | cube     | -18,16   |
| 5   | large  | red   | metal    | cylinder | 20,-4    |
| 6   | small  | green | metal    | sphere   | -8,-29   |
| 7   | small  | red   | metal    | cylinder | -20,-8   |
| 8   | medium | blue  | metal    | cube     | 2,-30    |
| 9   | large  | blue  | glass    | cube     | 23,-31   |

What are the indexes of objects that are changed?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 0, 1, 5
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2520
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Physical_Understanding;Physical_Reasoning
- **App**: Perception
- **Input Format**: 3D Models and Aerial Imagery
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'set_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
