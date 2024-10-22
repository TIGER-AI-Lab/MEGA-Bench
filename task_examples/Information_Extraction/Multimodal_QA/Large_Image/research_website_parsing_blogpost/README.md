# Task: Research website parsing blogpost

## Task Description:

```
Please read the blog post to answer the following question with short phrases or number.
```

![Image](o1_release.png)

## The 1-shot Example for Task Demonstration:

## Example Query:

```
Question: What percentile does gpt-o1-ioi achieve in Codeforce?
```

```
Demonstration example(s) of the task:
Example 1:
Example Question: What percentile does gpt-4o achieve in Codeforce?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 11th
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 6490
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Multimodal_QA;Large_Image
- **Application**: Information_Extraction
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'multi_ref_phrase'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Screenshots were taken of various ML research websites. Questions and answers were created by the annotator.
