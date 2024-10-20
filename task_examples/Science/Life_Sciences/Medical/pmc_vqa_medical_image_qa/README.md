# Task: pmc_vqa_medical_image_qa

## Task Description:

```
Answer a question based on the given medical image
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: What is represented by the yellow color in the merged image? PDGFRα proteins in red or The Golgi compartment in green
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: PDGFRα proteins in red
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1531
- **Eval Context**: {}
- **Taxonomy Tree Path**: Science;Life_Sciences;Medical
- **App**: Science
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
