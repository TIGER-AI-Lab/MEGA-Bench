# Task: Tqa textbook qa

## Task Description:

```
Answer the question based on an image taken from a textbook.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: How many actions are depicted in the diagram? Answer the question using a single word or phrase.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 7. seven
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1998
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Science;STEM
- **Application**: Science
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'multi_ref_phrase'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from Dvqa, and the questions and answers are refractered from the original TQA dataset
