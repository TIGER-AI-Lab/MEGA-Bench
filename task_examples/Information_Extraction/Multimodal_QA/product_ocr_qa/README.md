# Task: Product ocr qa

## Task Description:

```
Given an image of a product, answer questions about the product. Please only output the answer without any additional information.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: For what skin type is this product designed?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Dry skin
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3807
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Multimodal_QA
- **Application**: Information_Extraction
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were taken from various websites. Questions and answers were created by the annotator.
