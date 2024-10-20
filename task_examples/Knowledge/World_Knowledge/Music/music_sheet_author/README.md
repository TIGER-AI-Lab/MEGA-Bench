# Task: music_sheet_author

## Task Description:

```
Here is a piece of a piano sheet, please choose the correct author of this music sheet from the options.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](2-1.png)

![Image](2-2.png)

```
Example Question: Choose from the following options: Frédéric Chopin, Wolfgang Amadeus Mozart, Johann Sebastian Bach, Carl Philipp Emanuel Bach
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Frédéric Chopin
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3489
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Music
- **App**: Knowledge
- **Input Format**: Text-Based Images and Documents
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
