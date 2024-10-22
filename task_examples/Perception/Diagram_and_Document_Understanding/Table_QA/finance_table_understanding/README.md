# Task: Finance table understanding

## Task Description:

```
Please answer the question given a table and the question description. Make sure the final answer is in the format of "Answer: ...", and ignore the unit if any, unless specified otherwise.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](image_1.png)

```
Example Question: Without referring to the preprogrammed function on your financial calculator, use the basic formula for present value, along with the given opportunity cost, r, and the number of periods, n, to calculate the present value of $1 in case C shown in the following table. (Answer rounded to four decimal places)
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 0.8638
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 490
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Table_QA
- **Application**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'answer': 'general_single_numerical_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were collected from MMMU. Questions and answers were adapted by the annotator into direct numerical output format
