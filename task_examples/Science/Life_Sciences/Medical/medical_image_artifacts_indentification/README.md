# Task: Medical image artifacts indentification

## Task Description:

```
Given the medical endoscopy image, please observe what type of artifacts existing in the query image. The candidate artifact types are from (blood artifacts, blur, bubbles, instrument artifacts, low contrast, saturation, specularity).
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](145.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: saturation
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 2215
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Science;Life_Sciences;Medical
- **Application**: Science
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from GMAI-MMBench, and the questions and answers are adapted to match strings
