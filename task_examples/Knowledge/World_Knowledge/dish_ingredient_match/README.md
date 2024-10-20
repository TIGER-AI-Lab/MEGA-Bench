# Task: dish_ingredient_match

## Task Description:

```
Given an image of a prepared dish and a pool of candidate images, each representing different ingredients, the model's objective is to correctly identify and pair the dish with the image of the ingredients likely used in the dish. The output is the index of the ingredient image from the candidates, which is an integer starting from 1.
```

![Image](global_1.png)

![Image](global_2.png)

![Image](global_3.png)

![Image](global_4.png)

![Image](global_5.png)

![Image](global_6.png)

![Image](global_7.png)

![Image](global_8.png)

![Image](global_9.png)

![Image](global_10.png)

![Image](global_11.png)

![Image](global_12.png)

![Image](global_13.png)

![Image](global_14.png)

![Image](global_15.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2950
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'index': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'index': 1}}
  - **Response Parse Function**: answer_string
