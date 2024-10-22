# Task: Medical parasite detection

## Task Description:

```
Given a set of cell images including parasitized or uninfected cells in each example question, please detect which cell images reflect that they are infected with malaria. The answer should a list including the index of images. The first image has the index 1.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1_3.png)

![Image](1_0.png)

![Image](1_1.png)

![Image](1_2.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: [1, 2]
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3960
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Science;Life_Sciences;Medical
- **Application**: Science
- **Input Format**: Photographs
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'set_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from pdf screenshot, and the questions and answers are adapted to match set equality
