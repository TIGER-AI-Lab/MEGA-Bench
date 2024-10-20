# Task: worldle

## Task Description:

```
Identify the 1. country, 2. province or state, and 3. municipality where the photos where taken. Except for some rural areas, the municipality is usually the name of the city or town. The United States shall be called the ˋUnited Statesˋ.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](belgium_tournai_grand_place-1.png)

![Image](belgium_tournai_grand_place-2.png)

![Image](belgium_tournai_grand_place-3.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'country': 'Belgium', 'province_or_state': 'Hainaut', 'municipality': 'Tournai'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2978
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'country': 'exact_str_match', 'province_or_state': 'exact_str_match', 'municipality': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'country': 1, 'province_or_state': 2, 'municipality': 2, 'proximity': 5}}
  - **Response Parse Function**: json
