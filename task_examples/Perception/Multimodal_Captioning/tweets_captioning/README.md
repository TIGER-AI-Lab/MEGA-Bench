# Task: tweets_captioning

## Task Description:

```
You are going to share the given picture on a social media platform. Write a caption that best describes the picture.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](christmas.png)

```
Example Response: Answer: The True Spirit Of Christmas
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 537
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Multimodal_Captioning
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
