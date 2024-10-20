# Task: google_streetview_circle_reasoning

## Task Description:

```
The photographer is standing in a fixed place. He takes a photo every time he turns a certain angle until he returns to the starting point. The order of the following photos is disrupted. Please start from the first photo and sort the photos by turning right and then answer the question about at least how many images are there between selected two images. Your answer should be an integar. If the selected images are adjacent, your answer should be '0'.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1-1.png)

![Image](1-5.png)

![Image](1-3.png)

![Image](1-4.png)

![Image](1-6.png)

![Image](1-2.png)

![Image](1-7.png)

```
Example Question: For the image-1 and image-5 in the input, after they are correctly sorted into a circle, how many images are there between them at least? 
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3234
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;3D_understanding
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
