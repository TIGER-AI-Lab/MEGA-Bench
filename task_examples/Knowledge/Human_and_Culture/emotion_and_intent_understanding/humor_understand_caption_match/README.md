# Task: Humor understand caption match

## Task Description:

```
Your task is to determine which caption is appropriate for a given humorous cartoon. Your task is to select the most appropriate caption from the given candidates.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: [ "I couldn't put it down. In fact, I couldn't pick it up.", "First you must gain their trust.", "Of course, the current tenant will be gone before the first of the month.", "Must....return....new....puppy...", "Pardon me, can you draw clothes?" ]
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: First you must gain their trust.
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 748
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;Human_and_Culture;emotion_and_intent_understanding
- **Application**: Knowledge
- **Input Format**: Artistic and Creative Content
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images and labels come from a Humor Understanding benchmark derived from the New Yorker Caption Contest. Questions and answers were adapted by a human annotator.
