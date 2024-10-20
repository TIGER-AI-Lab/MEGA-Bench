# Task: google_streetview_direction_understanding

## Task Description:

```
This set of tasks involves analyzing and interpreting pairs of images, with the goal of determining the appropriate walking directions or route from one location to another.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](01_1.jpg)

![Image](1_2.jpg)

```
Example Question: If I want to walk from the location in Image 1 to the location in Image 2, should I turn left or right?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: turn left
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3305
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;3D_understanding
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
