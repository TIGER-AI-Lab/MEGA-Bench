# Task: Music sheet name

## Task Description:

```
Here is a piece of a musical sheet (in musical score), please find out which piece of music this five-line piano score comes from and what its name is, choose the correct option.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](2-1.png)

![Image](2-2.png)

```
Example Question: Choose from the following options: Marzuka, Moonlight Sonata, Für Elise, Nocturne in E-flat major, Rondo Alla Turca
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Marzuka
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3445
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Music
- **Application**: Knowledge
- **Input Format**: Text-Based Images and Documents
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images are music sheets posted to [Noteflight](https://www.noteflight.com/). Questions and answers were created by a human annotator.
