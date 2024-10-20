# Task: logo2k_same_type_logo_retrieval

## Task Description:

```
Given a list of brand logo pictures, find out which logo(s) belong to the same category as the first logo by answering a list of image index. Please also answer this category name. Possible logo categories include: Accessories, Clothes, Cosmetics, Electronics, Food, Institutions, Leisure, Medical, Necessities, and Transportation. Note that the index 1 should not be included as it's the query image.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](e1-1-cosmetic-ysl.png)

![Image](e1-2-cosmetic-watsons.png)

![Image](e1-3-cosmetic-olay.png)

![Image](e1-4-acc-churchs.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'logos of the same category': '[2, 3]', 'category name': 'Cosmetics'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 292
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Logo_and_Sign
- **App**: Knowledge
- **Input Format**: Text-Based Images and Documents
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'logos of the same category': 'set_equality', 'category name': 'exact_str_match_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'logos of the same category': 1, 'category name': 1}}
  - **Response Parse Function**: json
