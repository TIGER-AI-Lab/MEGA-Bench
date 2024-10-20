# Task: places365_scene_type_classification

## Task Description:

```
Given a query image and a set of candadate scene types, pick one scene type that best describes the image. Some options might have similar meanings, but only one choice can match the scene in the image most accurately.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](Places365_val_00002047.png)

```
Example Question: Candidate scene types: [candy_store, church_indoor, campsite, lobby, mountain, vegetable_garden, valley, forest_road, blue tent, picnic]
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: campsite
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1641
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Visual_Recognition
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'scene type': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'scene type': 1}}
  - **Response Parse Function**: answer_string
