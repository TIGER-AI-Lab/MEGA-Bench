# Task: Veracity

## Task Description:

```
Your task is to check If the image supports the truthfulness of the claim. The answer should follow the format "Answer: $BOOL". $BOOL is 1 if you think the image and text have good factual consistency, $BOOL is 0 otherwise.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](10324-53905-07-IvMVDZKDhFOMYr9ocAMeAB1ZHQdPtWhQ048kmuZ_9rM.png)

```
Example Question: A map showing the 'Distribution of Perching Birds' in a science textbook mistook Africa for South America.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5513
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;Fact_Checking
- **Application**: Knowledge
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images and labels come from the MFCBench dataset. Questions and annotations were adapted by a human annotator.
