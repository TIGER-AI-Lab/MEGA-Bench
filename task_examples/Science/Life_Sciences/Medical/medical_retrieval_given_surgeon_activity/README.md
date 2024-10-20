# Task: medical_retrieval_given_surgeon_activity

## Task Description:

```
Given the query endoscopy videos including multiple frames, please retrieve the video based on the given surgeon action in the example question. The answer should be an index of expected video. The index starts from 1.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](180.png)

![Image](185.png)

![Image](190.png)

![Image](195.png)

```
Example Question: bagging prostate
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3249
- **Eval Context**: {}
- **Taxonomy Tree Path**: Science;Life_Sciences;Medical
- **App**: Science
- **Input Format**: Videos
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
