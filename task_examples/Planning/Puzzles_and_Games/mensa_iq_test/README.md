# Task: Mensa iq test

## Task Description:

```
Based on the following set of images, which missing image fits the pattern best?

The images that are adjacent to each other at the top form the pattern. One of them is missing and you need to identify which one it is, among the given options at the bottom. These are the images that are spread further apart below the grid of images showing the pattern.

You will be provided a JSON schema and you must follow this schema to identify which option is the correct answer.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0.png)

```
Example Question: ˋˋˋjson
{
    "outer_shape": "str",
    "inner_shape": "str",
    "inner_shape_colour": "str"
}
ˋˋˋ
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'outer_shape': 'triangle', 'inner_shape': 'square', 'inner_shape_colour': 'black'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 2576
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games
- **Application**: Planning
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'answer': 'dict_precision'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from website, and the questions and answers are adapted to match dict equality
