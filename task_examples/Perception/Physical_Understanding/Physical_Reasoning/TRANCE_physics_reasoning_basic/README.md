# Task: Trance physics reasoning basic

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
| 0   | medium | yellow | metal    | cylinder | 5,-18    |
| 1   | large  | gray   | rubber   | sphere   | 19,40    |
| 2   | medium | gray   | glass    | cylinder | 2,39     |
| 3   | small  | cyan   | rubber   | cube     | -4,7     |
| 4   | small  | blue   | rubber   | cylinder | 12,2     |
| 5   | large  | yellow | metal    | cylinder | 13,-27   |
| 6   | large  | purple | rubber   | cube     | -10,-2   |
| 7   | medium | yellow | glass    | sphere   | -21,30   |
| 8   | medium | blue   | rubber   | sphere   | 30,34    |
| 9   | small  | gray   | glass    | sphere   | -14,18   |

Which object is changed?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 0
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3022
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Physical_Understanding;Physical_Reasoning
- **Application**: Perception
- **Input Format**: 3D Models and Aerial Imagery
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data are collected from Trance by specifically picking up samples with the easiest settings. Questions and answers are re-designed for this specific task
