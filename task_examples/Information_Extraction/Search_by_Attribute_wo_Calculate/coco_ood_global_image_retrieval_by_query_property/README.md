# Task: Coco ood global image retrieval by query property

## Task Description:

```
You are provided with a list of images. You will then be queried with various questions related to these images. You need to understand each question and find out the image(s) that satisfy the requirements. When there are multiple choices, sort them based on the order in the image list.
```

![Image](cartoon_000000000186.png)

![Image](cartoon_000000000376.png)

![Image](cartoon_000000000721.png)

![Image](painting_000000000900.png)

![Image](painting_000000000912.png)

![Image](sketch_000000000165.png)

![Image](sketch_000000000521.png)

![Image](tattoo_000000000470.png)

![Image](tattoo_000000000496.png)

![Image](tattoo_000000000535.png)

![Image](weather_000000000824.png)

## The 1-shot Example for Task Demonstration:

## Example Query:

```
Question: Which image(s) are in cartoon style? Note that sketches and paintings are not considered as being cartoon-style.
```

```
Demonstration example(s) of the task:
Example 1:
Example Question: Which images contain car(s)?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: [1, 2, 11]
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1224
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Search_by_Attribute_wo_Calculate
- **Application**: Information_Extraction
- **Input Format**: Artistic and Creative Content
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'image ids': 'jaccard_index'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'image ids': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were from COCO-O. Questions and answers were re-designed by the annotator manually
