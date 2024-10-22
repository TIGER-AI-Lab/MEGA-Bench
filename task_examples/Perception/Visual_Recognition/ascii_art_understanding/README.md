# Task: Ascii art understanding

## Task Description:

```
Given an ascii art image and a question, select the most matched object name and answer the letter option.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1012.png)

```
Example Question: What is depicted in the above ASCII art? A: eye B: face C: buttock D: hand
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: B
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 2318
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Visual_Recognition
- **Application**: Perception
- **Input Format**: Text-Based Images and Documents
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data and annotations were collected and created by the annotator from various online resources
