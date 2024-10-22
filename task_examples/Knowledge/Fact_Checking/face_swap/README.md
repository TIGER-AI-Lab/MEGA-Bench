# Task: Face swap

## Task Description:

```
Your task is to determine if the face in the image has been swapped to change the identity. You will be give the caption and the image, and you should recognize individuals and use your prior knowledge about the individuals to make a judgement. The answer should follow the format "Answer: $BOOL". $BOOL is 1 if you think the face has been swapped, $BOOL is 0 otherwise.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1264472_face_swap.png)

```
Example Question: Afua Hirsch at Fleur de Chou primary school in Croix des Bouquets Read her report on school after the earthquake on educationguardiancouk
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5457
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;Fact_Checking
- **Application**: Knowledge
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images and labels come from the MFCBench dataset. Questions and annotations were adapted by a human annotator.
