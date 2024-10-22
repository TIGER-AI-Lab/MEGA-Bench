# Task: Autorater unmask

## Task Description:

```
A tuple of (given image, output image) is given. A model tries to edit the given image based on an editing instruction and produces an output image. You need to rate the quality of the output image based on how well it aligns with the instruction and how realistic it is. You are supposed to output "good", "medium" or "bad".
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](orig_1.png)

![Image](output_1.png)

```
Example Question: Editing Instruction: Make the doll wear a hat.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: medium
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5597
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Metrics;Generated_Image_Eval
- **Application**: Metrics
- **Input Format**: Artistic and Creative Content
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'rating': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'rating': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were collected from ImagenHub. Questions and answers adapted by the annotator
