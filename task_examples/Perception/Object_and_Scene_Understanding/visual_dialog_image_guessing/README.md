# Task: visual_dialog_image_guessing

## Task Description:

```
Given a dialogue that discusses an image, each dialogue consists of ten question-and-answer pairs. The person asking the questions cannot see the image, while the person answering the questions can see it. You need to identify which image from the candidate images is being discussed in this dialogue. You should provide the index of the target image within all the candidates, which is an integer starting from 1.
```

![Image](1.png)

![Image](2.png)

![Image](3.png)

![Image](4.png)

![Image](5.png)

![Image](6.png)

![Image](7.png)

![Image](8.png)

![Image](9.png)

![Image](10.png)

![Image](11.png)

![Image](12.png)

![Image](13.png)

![Image](14.png)

![Image](15.png)

![Image](16.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
Example Question: [ [ "is the photo in color", "yes" ], [ "is it a professional photo", "no" ], [ "is it well lit", "no" ], [ "is it daytime", "i don't see windows" ], [ "does this look like an adults bedroom", "maybe" ], [ "is the room clean", "no" ], [ "can you tell what kind of computer it is", "no not really" ], [ "is it a flat screen", "yes" ], [ "what's the desk made out of", "cheap plastic or wood" ], [ "is there a computer chair", "yes" ] ]
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 395
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Object_and_Scene_Understanding
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'image id': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'image id': 1}}
  - **Response Parse Function**: answer_string