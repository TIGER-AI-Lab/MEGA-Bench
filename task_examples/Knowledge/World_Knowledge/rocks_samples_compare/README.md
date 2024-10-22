# Task: Rocks samples compare

## Task Description:

```
Imagine you are a college student studying geology. Compare the two or three images of some rocks and tell whether they are of the same kind. Your output should be 'Yes' or 'No'.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](002.png)

![Image](003.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Yes
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 2562
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge
- **Application**: Knowledge
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images and labels come from [ChinaNeolithic.com](http://chinaneolithic.com/en/Rock/)'s online rock store. Questions were created by a human annotator.
