# Task: logical_reasoning_2D_views_of_3D_shapes

## Task Description:

```
Given a 3D figure on the first image and multiple 2D views on the remaining ones, please select the correct 2D views of 3D shapes based on the proposed view types in the per example question. The answer should be a dictionary where the key is the view type and value is the image index of correct 2D views. The image indexs are represented by letter and follows: (a: sthe second image; b: the third image; c: the forth image; b: ....)
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](web-1.png)

![Image](web-1-2.png)

![Image](web-1-3.png)

![Image](web-1-4.png)

![Image](web-1-5.png)

```
Example Question: What is the top-down view of 3D shape?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'top-down': 'c'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2802
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games
- **App**: Planning
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'dict_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
