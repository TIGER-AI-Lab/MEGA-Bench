# Task: Music sheet note count

## Task Description:

```
Here is a piece of a musical sheet (in musical score or simplified score), please count the number of notes that meet certain requirements.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1-2.png)

```
Example Question: How many notes that lie exactly on the bottom line (first line) are there in musical notationin?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 11
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4253
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Music
- **Application**: Knowledge
- **Input Format**: Text-Based Images and Documents
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images are music sheets posted to [Noteflight](https://www.noteflight.com/). Questions and answers were created by a human annotator.
