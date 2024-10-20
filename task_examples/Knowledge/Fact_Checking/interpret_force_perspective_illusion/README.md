# Task: interpret_force_perspective_illusion

## Task Description:

```
Given a picture with forced perspective optical illusion, indicate which entity appear to be much smaller than normal with the illusion. A set of entity names will be provided, and you will need to pick the one that is most relevant to the illusion effect.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](e1.png)

```
Example Question: Candidate entities: ball, man, sky, tree, meadow
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: man
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2716
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;Fact_Checking
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
