# Task: Autorater mask

## Task Description:

```
You are presented with a triple of (input image, mask, output image). An image generation model receives the input image, a mask, and an editing instruction to produce the output image. Your task is to judge the quality of the output image based on how well the output image aligns with the input image, the editing instruction, and the mask. You are supposed to produce "good", "medium" or "bad"
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](orig_1.png)

![Image](mask_1.png)

![Image](output_1.png)

```
Example Question: Editing instruction: make the zebra open its mouth
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: medium
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5653
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Metrics;Generated_Image_Eval
- **Application**: Metrics
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'rating': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'rating': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were collected from ImagenHub. Questions and answers adapted by the annotator
