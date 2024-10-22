# Task: Autorater 3d model texturing

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

## Additional Information:

- **Sample ID**: 5710
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Metrics;Generated_Image_Eval
- **Application**: Metrics
- **Input Format**: 3D Models and Aerial Imagery
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'sequence_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Resources are collected from the user study of~\citet{Perla2024EASITexEM}. Questions and answers were designed and created by the annotator
