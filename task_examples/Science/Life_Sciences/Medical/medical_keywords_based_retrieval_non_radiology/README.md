# Task: medical_keywords_based_retrieval_non_radiology

## Task Description:

```
Given a set of query medical non-radiology images, please retrieve the index of the image based on the given keywords in example question. The keywords are separated by commas. The indexs of images are represented by (A, B, C, D, ...). The answer should be the letter.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](ROCO_81827.png)

![Image](ROCO_82100_1.png)

![Image](ROCO_82109_1.png)

![Image](ROCO_82152_1.png)

```
Example Question: demineralized,	slurrygroup	enamel,	pumouse	prophylaxi,	electron,	microscopy,	magnification,	original
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: A
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4284
- **Eval Context**: {}
- **Taxonomy Tree Path**: Science;Life_Sciences;Medical
- **App**: Science
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
