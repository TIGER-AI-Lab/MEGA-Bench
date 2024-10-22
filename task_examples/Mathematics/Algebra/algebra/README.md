# Task: Algebra

## Task Description:

```
Please answer the algebra-related question given a corresponding diagram. Make sure the answer is in the format of "Answer: ...", and ignore the unit if any.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](image_1.png)

```
Example Question: Five cards are lying on the table in the order 1,3,5,4,2. You must get the cards in the order $1,2,3,4,5$. Per move, any two cards may be interchanged. How many moves do you need at least?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 2
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 646
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Mathematics;Algebra
- **Application**: Mathematics
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'general_single_numerical_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from MathVision, and the questions and answers are adapted by human annotator
