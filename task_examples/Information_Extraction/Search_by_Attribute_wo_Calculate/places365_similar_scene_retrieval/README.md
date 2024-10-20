# Task: places365_similar_scene_retrieval

## Task Description:

```
There are a set of images in the database. Given a new query image, your task is to pick one image from the database that best matches the scene semantics of the query image. Return the index of the image in the database. The index starts from 1. If there is no proper match, please answer NA.
```

![Image](arch-1.png)

![Image](assembly-line-1.png)

![Image](auto-showroom-1.png)

![Image](badlands-1.png)

![Image](dam-1.png)

![Image](fastfood_restaurant-1.png)

![Image](food_court-1.png)

![Image](gas_station-1.png)

![Image](greenhouse-1.png)

![Image](harbor-1.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](arch-2.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 40
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Search_by_Attribute_wo_Calculate
- **App**: Information_Extraction
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
