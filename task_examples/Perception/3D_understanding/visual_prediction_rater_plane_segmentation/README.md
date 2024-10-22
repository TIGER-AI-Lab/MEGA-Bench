# Task: Visual prediction rater plane segmentation

## Task Description:

```
The ability to detect plane is important for 3D understanding. Your task is to rate the quality of several plane segmentation results. Given an input picture taken in an indoor space and a list of plane segmentation results, you should rank from the best-quality result to the worst. Pixels of the same plane have the same color in the results. You should judge the quality based on consistency with input image (i.e., the first image provided to you), alignments with the correct 3D commonsense, and quality of the planes. Mistakes on common plane structures like walls or floors should be peanalized harshly. \n\nThe first image of each query is the input, and the remaining images are the results to be rated. Your answer should be a sequence of index. The first result has index 1. Do not count the input image into the index.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](e1-input.png)

![Image](e1-1.png)

![Image](e1-2.png)

![Image](e1-3.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 3, 2, 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4691
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;3D_understanding
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'sequence_accuracy_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were collected by taking screenshots from plane segmentation papers on arXiv
