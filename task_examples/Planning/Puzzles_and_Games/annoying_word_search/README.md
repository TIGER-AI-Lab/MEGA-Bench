# Task: Annoying word search

## Task Description:

```
Find all of the words in the word search. In the returned solution, the keys should use the capitalization and punctuation used in the word list. Use 1-based indexing. For the co-ordinates, the column goes before the row.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'arrear': [[[20, 7], [15, 2]]], 'rarer': [[[19, 7], [15, 3]]], 'rearer': [[[3, 12], [8, 17]]], 'airier': [[[9, 15], [4, 20]]], 'eerie': [[[15, 8], [11, 8]]], 'reiterate': [[[11, 9], [3, 9]]], 'irritate': [[[6, 7], [6, 14]]], 'terraria': [[[13, 19], [6, 12]]], 'attire': [[[18, 19], [13, 14]]], 'retreat': [[[11, 13], [17, 7]]], 'aerate': [[[9, 18], [9, 13]], [[17, 3], [17, 8]], [[20, 14], [15, 9]]], 'errata': [[[1, 17], [6, 12]]], 'tiara': [[[14, 17], [18, 13]]], 'trait': [[[17, 19], [13, 19]], [[13, 19], [9, 19]]], 'retiree': [[[6, 15], [12, 9]]], 'terrier': [[[14, 17], [8, 17]]]}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 2702
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games
- **Application**: Planning
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'word_locations': 'dict_jaccard_agg_jaccard'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'word_locations': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from various websites, and the answers are annotated by human annotator
