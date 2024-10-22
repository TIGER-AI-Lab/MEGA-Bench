# Task: Landmark check two images

## Task Description:

```
Given a pair of landmark images, answer three questions: (1). Are the two landmarks the same? (2). Are they in the same image style (photograph, sketch painting, cartoon are all different styles)? (3). Are the two landmarks in the same country? Answer yes or no for each question.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](e1-88197_Schloss_Rudenhausen_1.png)

![Image](e1-Rudenhausen_Schloss_2.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'same landmark': 'yes', 'same style': 'no', 'same country': 'yes'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1955
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Landmark_and_Buliding
- **Application**: Knowledge
- **Input Format**: Artistic and Creative Content
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'same landmark': 'exact_str_match_case_insensitive', 'same style': 'exact_str_match_case_insensitive', 'same country': 'exact_str_match_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'same landmark': 1, 'same style': 1, 'same country': 1}}
  - **Response Parse Function**: json
- **Source Description**: Images and labels come from the Landmark v2 dataset. Questions and answers were adapted by a human annotator.
