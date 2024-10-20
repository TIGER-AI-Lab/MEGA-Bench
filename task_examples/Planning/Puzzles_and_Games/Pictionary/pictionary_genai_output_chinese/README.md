# Task: pictionary_genai_output_chinese

## Task Description:

```
Look at the provided image and question, guess which Chinese word or phrase the image is trying to convey. Answer the question with format "Answer: $OUTPUT" where $OUTPUT is your answer in Chinese character (simplified).
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: 图中表示的是何种四字食物？
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 驴肉火烧
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 6334
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games;Pictionary
- **App**: Planning
- **Input Format**: Artistic and Creative Content
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
