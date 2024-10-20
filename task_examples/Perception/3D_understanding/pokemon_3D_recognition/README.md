# Task: pokemon_3D_recognition

## Task Description:

```
You will be provided with an index of Pokémon, which contains their images, nicknames, and CP values. Some random views of a Pokémon is given, and the task is to recognize the Pokémon, finding its location in the index (use X-Y-Z format, where X is image index, Y is the row index, and Z is the column index. The index starts at 1), then answering its nickname and CP value.
```

![Image](index_1.png)

![Image](index_2.png)

![Image](index_3.png)

![Image](index_4.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](Altaria_1.png)

![Image](Altaria_2.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'nickname': 'Altaria', 'cp': '1491', 'location': '3-1-3'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4495
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;3D_understanding
- **App**: Perception
- **Input Format**: 3D Models and Aerial Imagery
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'nickname': 'exact_str_match', 'cp': 'exact_str_match', 'location': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'nickname': 1, 'cp': 1, 'location': 2}}
  - **Response Parse Function**: json
