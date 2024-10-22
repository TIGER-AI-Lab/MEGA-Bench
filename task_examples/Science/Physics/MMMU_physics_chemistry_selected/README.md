# Task: Mmmu physics chemistry selected

## Task Description:

```
Given the college level physics or chemistry Mulitple Choice Question, output the correct option.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: Choose from the following options: ['To the right/To the right', 'To the right/To the left','To the left/To the right', 'No direction; the force is zero./To the left']
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: To the right/To the right
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4224
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Science;Physics
- **Application**: Science
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from MMMU, and the questions and answers are adapted to match strings
