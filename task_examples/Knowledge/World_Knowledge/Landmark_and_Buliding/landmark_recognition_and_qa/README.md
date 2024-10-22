# Task: Landmark recognition and qa

## Task Description:

```
Given a photograph of a landmark, answer 1) the landmark's name, 2) the city of the landmark, and 3) the country of the landmark. All answers should use English letters. Some hints will be given if there are multiple possible landmarks in the image.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](11525_St_Lawrence_Hall_Toronto.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'landmark name': 'St. Lawrence Hall', 'city': 'Toronto', 'country': 'Canada'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1459
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Landmark_and_Buliding
- **Application**: Knowledge
- **Input Format**: Photographs
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'landmark name': 'near_str_match', 'city': 'multi_ref_phrase', 'country': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'landmark name': 1, 'city': 1, 'country': 1}}
  - **Response Parse Function**: json
- **Source Description**: Images and labels come from the Landmark v2 dataset. Questions and answers were adapted by a human annotator.
