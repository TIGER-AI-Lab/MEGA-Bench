# Task: text_style

## Task Description:

```
Your task is to determine if the text description's style have been manipulated on purpose, based on the given image. You will be give the caption and the image. The answer should follow the format "Answer: $BOOL". $BOOL is 1 if you think the text has been manipulated to change the style, $BOOL is 0 otherwise.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](42141.png)

```
Example Question: Yellen flanked by Organization for Economic Cooperation and Development SecretaryGeneral Jose Angel Gurria left and British Chancellor of the Exchequer George Osborne attends a meeting of the G20 finance ministers and central bank governors in Shanghai in February
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 0
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5471
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;Fact_Checking
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
