# Task: ancient_map_understanding

## Task Description:

```
You are provided with an ancient map showing various historical states, along with the name of a current city. Your task is to identify which ancient state this city belonged to. Note: use the characeter in the given image to answer the question.
```

![Image](zhanguo_280_ac.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](zhanguo_280_ac.png)

```
Example Question: 北京
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 燕
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2405
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge
- **App**: Knowledge
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
