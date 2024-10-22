# Task: Human relationship reasoning

## Task Description:

```
Judge the relationship between people in this image
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: What could be the relationship between the two people on the far left and far right? Choose from couple, friends, parent-child, or colleagues?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: couple
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1096
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;Human_and_Culture
- **Application**: Knowledge
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images come from various websites. Questions and annotations were created by a human annotator.
