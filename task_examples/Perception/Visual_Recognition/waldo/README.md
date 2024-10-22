# Task: Waldo

## Task Description:

```
In the following image, we have five characters from left to right: ˋodlawˋ, ˋwhitebeardˋ, ˋwendaˋ, ˋwoofˋ (or his tail), and ˋwaldoˋ. Please find the bounding boxes for these characters in the following images. The format of bounding box is (x1, y1, x2, y2), where (x1, y1) is the top-left corner and (x2, y2) is the bottom-right corner. The coordinates are normalized by the image's height and width, and each value has three significant digits.
```

![Image](global.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0.png)

```
Example Question: You must find the following characters: ˋwaldoˋ, ˋwendaˋ.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'waldo': '(0.165, 0.709, 0.176, 0.740)', 'wenda': '(0.319, 0.828, 0.329, 0.864)'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4186
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Visual_Recognition
- **Application**: Perception
- **Input Format**: Artistic and Creative Content
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'bounding_boxes': 'dict_nbbox_iou_tuple_agg_jaccard'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'bounding_boxes': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images and annotations were collected and created by the annotator using various resources on the Web
