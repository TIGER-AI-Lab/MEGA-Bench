# Task: Adapted cvbench relation

## Task Description:

```
You are a multimodal AI assistant and your goal is to answer the following question on a visual question on object relation. Answer between 'left', 'right', 'below', 'above', 'in front', and 'behind'.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](img_2D_relation_coco_203.png)

```
Example Question: Considering the relative positions of the book (annotated by the red box) and the couch in the image provided, where is the book (annotated by the red box) located with respect to the couch?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: left
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4904
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Spatial_Understanding
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from CV-Bench's relation split, and adapted into exact text answer
