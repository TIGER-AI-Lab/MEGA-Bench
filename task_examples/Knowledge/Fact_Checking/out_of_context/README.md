# Task: out_of_context

## Task Description:

```
Your task is to evaluate the coherence and correspondence of context for the given image and text. You will be give the caption and the image. The answer should follow the format "Answer: $BOOL". $BOOL is 1 if you think the image and text are contextually well aligned, $BOOL is 0 otherwise.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](620701.png)

```
Example Question: Saudi troops cheer as they ride at the back of an army truck in the southwestern province of Jizan near the border with Yemen
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5485
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;Fact_Checking
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
