# Task: Medical abdomen mri organ recognition

## Task Description:

```
Given the MRI medical images in the Abdomen, please recognize which organs can appropriately describe the marked areas in the given query images. The answer should be a list including the organ types that represent the query images in order. The answer should be selected from (adrenal gland, duodenum, gallbladder, large intestine, pancreas, small intestine, spleen, stomach)
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1029.png)

![Image](1039.png)

![Image](1089.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: stomach, large intestine, small intestine
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 2816
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Science;Life_Sciences;Medical
- **Application**: Science
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'sequence_accuracy_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from GMAI-MMBench, and the questions and answers are adapted to match sequence accuracy
