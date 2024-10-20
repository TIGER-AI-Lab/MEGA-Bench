# Task: autorater_subject

## Task Description:

```
You are given a subject image. A model tries to put this subject under a different context based on the prompt. You need to rate whether the model-generated image is good in terms of its consistency with the given subject image, the prompt, and realisticness. Please answer with "good", "medium" or "bad".
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](sample_0.png)

![Image](output_1.png)

```
Example Question: Prompt: A backpack in paris
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: bad
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5667
- **Eval Context**: {}
- **Taxonomy Tree Path**: Metrics;Generated_Image_Eval
- **App**: Metrics
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Rating': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Rating': 1}}
  - **Response Parse Function**: answer_string
