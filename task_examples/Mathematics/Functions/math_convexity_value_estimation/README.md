# Task: Math convexity value estimation

## Task Description:

```
You are given a real-valued, scalar function f(x).
YOUR TASK is to determine whether f(x) is an convex function or an concave function, and then estimate the value of the function when x=15
- Definition of a convex function: 
A function such that for all x, y, and 0 <= t <= 1, f(tx + (1 − t)y) ≤ t f(x) + (1 − t)f(y)
- Definition of a concave function: 
A function such that for all x, y, and 0 <= t <= 1, f(tx + (1 − t)y) ≥ t f(x) + (1 − t)f(y)
Respond first with ‘convex’ or ‘concave’ on whether the function f(x) is convex or concave. Then the value of the function in integer, when x=15. Write down all the digits and DO NOT use the scientific format (such as 1E5). Answer with format " {"convexity": ..., "value": ...}  " .
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](c_1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'convexity': 'convex', 'value': '46'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1025
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Mathematics;Functions
- **Application**: Mathematics
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'convexity': 'exact_str_match', 'value': 'number_rel_diff_ratio'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'convexity': 1, 'value': 3}}
  - **Response Parse Function**: json
- **Source Description**: Data collected from IsoBench, and the questions and answers are adapted by human annotator
