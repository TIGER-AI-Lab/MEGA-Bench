# Task: insect_order_classification

## Task Description:

```
This task involves the classification of insects into their respective taxonomic orders based on visual input. The goal is to accurately identify and categorize an insect from an image into one of the pre-defined orders. Each order is represented by a specific label corresponding to the insect's taxonomic classification, including orders such as Diptera, Hymenoptera, Coleoptera, Hemiptera, Lepidoptera, Psocodea, Thysanoptera, Trichoptera, Orthoptera, Blattodea, Neuroptera, Ephemeroptera, Dermaptera, Archaeognatha, Plecoptera, or Embioptera.
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
Answer: Diptera
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 410
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Results': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Results': 1}}
  - **Response Parse Function**: answer_string
