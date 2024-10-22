# Task: Realworld qa en2cn

## Task Description:

```
Please answer the following question with one or two Chinese characters (simplified), do not use English in the answer, omit the unit.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](Figure1.png)

```
Example Question: Which direction is the one way sign pointing?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 右
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3662
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Multimodal_QA
- **Application**: Information_Extraction
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'output': 'multi_ref_phrase'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'output': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images and annotations were adapted from the RealWorldQA benchmark by the human annotator into an open-ended question. The translation requirement was added by the human annotator.
