# Task: Autonomous driving scene analysis

## Task Description:

```
Given an image observed when driving a car, you need to answer the corresponding question based on common traffic rules and your understanding of the scene.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: What is the license plate number of the truck in front?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 沪FSO632
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4573
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Object_and_Scene_Understanding
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images are collected from the Internet, questions and answers are designed by annotator
