# Task: Extract webpage headline

## Task Description:

```
Extract the headline from the screenshot of a website. If a subheadline exists, Separate it with the main headline using a period.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Discover, Appreciate, & Understand the Animal World!
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3865
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Visual_Recognition
- **Application**: Perception
- **Input Format**: User Interface Screenshots
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were collected from VisualWebBench. Questions and answers were adapted by the annotator
