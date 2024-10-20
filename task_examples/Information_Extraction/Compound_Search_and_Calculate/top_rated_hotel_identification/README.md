# Task: top_rated_hotel_identification

## Task Description:

```
Given a screenshot from a hotel booking website, identify the name of the highest-rated hotel based on the image.  If multiple hotels share the highest rating, provide a list of their names separated by comma.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](top_rated_hotel_identification1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Elite studio Suite MGM Signature with Strip View
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 925
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Compound_Search_and_Calculate
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'str_set_equality_comma'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
