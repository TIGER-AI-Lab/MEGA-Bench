# Task: Logical reasoning 2d folding

## Task Description:

```
Given the query image including a 2D foldable sheet (the first image) and several options for the folded 3D objects (the remaining images), please find out which 3D object comes from the 2D sheet. The answer should the image index starting from 1 that represents the second image.
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
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 2
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4312
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games
- **Application**: Planning
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Correct option': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Correct option': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from website, and the questions and answers are adapted to match strings
