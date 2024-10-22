# Task: Adapted cvbench distance

## Task Description:

```
You are a multimodal AI assistant and your goal is to answer the following question on a visual question on distance estimation. Choose between the provided options.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](img_3D_distance_omni3d_hypersim_162.png)

```
Example Question: Estimate the real-world distances between objects in this image. Which object is closer to the desk (highlighted by a red box), the shelves (highlighted by a blue box) or the books (highlighted by a green box)?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: shelves
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4862
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Spatial_Understanding
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from CV-Bench's distance split, and adapted into exact text answer
