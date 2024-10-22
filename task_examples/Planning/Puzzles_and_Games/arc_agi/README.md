# Task: Arc agi

## Task Description:

```
Your task is to solve the ARC-AGI problem. The NxM output grid cells should contain numbers from 0 to 9. Each digit represents a color (The first image below presents the color-to-index mapping. Black: 0, Blue: 1, Red: 2, Green: 3 Yellow: 4, Gray: 5, Purple: 6, Orange: 7, Cyan: 8, Dark red: 9). You are then given several image(s) showing example input-output pairs (left is input, right is output), which illustrates some patterns over the colored grids. Please solve the new query (the last image provided) using the discovered patterns. Provide the answer using digits as defined by the color mapping. The final answer should follow the format of "Answer: ˋˋˋ
 the NxM grid of digits 
ˋˋˋ ".
```

![Image](output_cells.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0_ex.png)

![Image](0_input.png)

```
Example Question: The output shape is 11x12.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 33333333333
00002000020
00002000020
33333333333
00002000020
00002000020
00002000020
11111111111
00002000020
11111111111
00002000020
00002000020
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1068
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games
- **Application**: Planning
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from [https://arcprize.org/play](https://arcprize.org/play) and the task is adapted from Intelligence, the question and answer are adapted into a grid of digits by human annotator
