# Task: autorater_motion_guided_editing

## Task Description:

```
Motion-guided image editing is important for generating realistic and context-aware animation. Your task is to rank the motion-guided image generation results. The desired motion is described by a text input, several generative models try to edit the input image based on the described motion. You should rate the generation results based on 1) how well the generated image follows the motion described by the text query and 2) whether the generated image is still consistent with the source image in terms of semantics and object attributes.

The first image is the source image; the rest are the edited results. Rank the results using their indices, starting with 1. Exclude the source image from the ranking.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0-0.png)

![Image](0-1.png)

![Image](0-2.png)

![Image](0-3.png)

```
Example Question: tilt the head to the left
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1, 2, 3
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5625
- **Eval Context**: {}
- **Taxonomy Tree Path**: Metrics;Generated_Image_Eval
- **App**: Metrics
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Order': 'sequence_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Order': 1}}
  - **Response Parse Function**: answer_string
