# Task: reward_models_t2i_reward

## Task Description:

```
Two model generate two images based on a given prompt. You need to rate which one is better. Please respond with "left" or "right" or "tie"
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](o_1_1.png)

![Image](o_1_2.png)

```
Example Question: Prompt: a cute dog is playing a ball
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: left
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 6405
- **Eval Context**: {}
- **Taxonomy Tree Path**: Metrics;Reward_Models
- **App**: Metrics
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Chosen': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Chosen': 1}}
  - **Response Parse Function**: answer_string
