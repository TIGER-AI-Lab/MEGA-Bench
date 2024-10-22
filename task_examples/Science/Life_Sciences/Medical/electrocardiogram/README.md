# Task: Electrocardiogram

## Task Description:

```
Is the electrocardiogram normal or abnormal and is there some problem. Output '1' for normal and '0' for abnormal. If it's abnormal, please also provide a initial diagnosis.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1x.png)

```
Example Response: Answer: 0, first degree atrioventricular block
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Information:

- **Sample ID**: 696
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Science;Life_Sciences;Medical
- **Application**: Science
- **Input Format**: Text-Based Images and Documents
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from MMMU, and the answers are open-ended
