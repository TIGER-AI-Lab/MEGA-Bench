# Task: Text entity replace

## Task Description:

```
Your task is to determine if the text description's entities have been replaced or edited to change the contexts based on the given image. You will be give the caption and the image. The answer should follow the format "Answer: $BOOL". $BOOL is 1 if you think the text has been manipulated to change the context, $BOOL is 0 otherwise.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](589493.png)

```
Example Question: Lady Kinnock said Tony Blair has the full backing of the British government to become the first president of the EU
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5415
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
