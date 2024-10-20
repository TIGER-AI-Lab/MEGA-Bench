# Task: super_clevr_scene_understanding

## Task Description:

```
Answer a math-related question based on a image rendered by Blender. Some definitions: "A is behind B means" A is closer to the camera than B.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: Are there the same number of big cyan metallic jets and purple bicycles? Answer the question using a single word without punctuation
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: No
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 145
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Object_and_Scene_Understanding
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'multi_ref_phrase'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
