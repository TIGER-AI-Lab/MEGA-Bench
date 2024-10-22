# Task: Table understanding fact verification

## Task Description:

```
Judge whether the claims about the given image are entilaed or refuted by the table. You need to answer with a dictionary like {'A': 'entailed/refuted', 'B': 'entailed/refuted', ...}.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](f1.png)

```
Example Question: A: mathieu garon be a player in the 2nd round.
B: switzerland have a position of left wing , and a round greater than 4 , with timo vertala as the player.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'A': 'entailed', 'B': 'refuted'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4964
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Table_QA
- **Application**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'output': 'dict_precision'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'output': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Tables were collected from WikiTableQuestions and TabFact. Questions and answers were designed by the annotator
