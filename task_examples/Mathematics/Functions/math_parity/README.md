# Task: Math parity

## Task Description:

```
You are given a plot of a real-valued, scalar function f(x).
YOUR TASK is to determine whether f(x) is an even function, an odd function, or neither.
- Definition of an even function: 
A function such that, f(x) = f(−x), where the value remains unchanged if the sign of the independent variable is reversed.
- Definition of an odd function: 
A function such that, f(−x) = −f(x), where the sign is reversed but the absolute value remains the same if the sign of the independent variable is reversed.
- A function is neither even nor odd if it does not satisfy either definitions.
Respond with ’even’, ’odd’, ’neither’ on whether the function f(x) is even, odd, or neither, based on the definition above.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](p_1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: odd
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 54
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Mathematics;Functions
- **Application**: Mathematics
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from IsoBench, and the questions and answers are adapted by human annotator
