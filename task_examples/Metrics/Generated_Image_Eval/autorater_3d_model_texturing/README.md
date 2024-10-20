# Task: autorater_3d_model_texturing

## Task Description:

```
You will be asked to evaluate the quality of textured 3D models by comparing two texture transfer results. The first image will show an untextured 3D model and a source image whose texture needs to be transferred to the mesh. The second image will show two textured 3D models for comparison, and you should pick one with better texturing quality (left or right), considering 1) the realisticness of the textured object; 2) the consistency between the textured mesh and the source image.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1_1.png)

![Image](1_2.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: left
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5710
- **Eval Context**: {}
- **Taxonomy Tree Path**: Metrics;Generated_Image_Eval
- **App**: Metrics
- **Input Format**: 3D Models and Aerial Imagery
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'sequence_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
