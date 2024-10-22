# Task: Medical content based retrieval radiology

## Task Description:

```
Given a set of query medical radiology images, please retrieve the index of the image based on the given description in example question. The indexs of images are represented by (A, B, C, D, ...). The answer should be the letter.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](ROCO_00002.png)

![Image](ROCO_00003.png)

![Image](ROCO_00004.png)

![Image](ROCO_00007.png)

```
Example Question: Computed tomography scan in axial view showing obliteration of the left maxillary sinus.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: A
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4397
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Science;Life_Sciences;Medical
- **Application**: Science
- **Input Format**: Text-Based Images and Documents
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer ': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer ': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from ROCO dataset, and the questions and answers are adapted to match strings
