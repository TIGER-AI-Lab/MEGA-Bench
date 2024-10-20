# Task: TRANCE_physics_reasoning_event

## Task Description:

```
You will be given 2 images, the start and end state of a system respectively. You will be given a list of items, with their index, size, color, material, shape and position. You should answer the question based on the given information. Note that not all the objects in the list is shown in the picture.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](10.png)

![Image](11.png)

```
Example Question: | obj | size   | color  | material | shape    | position |
|-----|--------|--------|----------|----------|----------|
| 0   | large  | cyan   | metal    | sphere   | 3,20     |
| 1   | medium | blue   | rubber   | cube     | 19,-13   |
| 2   | medium | yellow | metal    | cylinder | 30,-31   |
| 3   | medium | cyan   | rubber   | cube     | -18,6    |
| 4   | large  | green  | glass    | sphere   | -19,-5   |
| 5   | medium | yellow | glass    | sphere   | 30,0     |
| 6   | small  | red    | rubber   | sphere   | -9,-14   |
| 7   | small  | gray   | glass    | cylinder | 14,-36   |
| 8   | medium | brown  | metal    | cube     | -15,-29  |
| 9   | medium | green  | rubber   | cylinder | 14,8     |

What are the indexes of objects that are changed?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 0, 1, 4, 9
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3154
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Physical_Understanding;Physical_Reasoning
- **App**: Perception
- **Input Format**: 3D Models and Aerial Imagery
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'set_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
