# Task: stock_info_retrieval

## Task Description:

```
Given a set of screenshots from an interactive stock market chart and related details, retrieve the company names that match the specific query. Provide a list of company names separated by commas: ['Company 1', 'Comnany 2', ...]
```

![Image](stock_info_retrieval1.png)

![Image](stock_info_retrieval2.png)

![Image](stock_info_retrieval3.png)

![Image](stock_info_retrieval4.png)

![Image](stock_info_retrieval5.png)

![Image](stock_info_retrieval6.png)

![Image](stock_info_retrieval7.png)

![Image](stock_info_retrieval8.png)

![Image](stock_info_retrieval9.png)

![Image](stock_info_retrieval10.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
Example Question: Find the company with a highest Previous Close price.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: ['Tesla, Inc. (TSLA)']
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1272
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Compound_Search_and_Calculate
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'set_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
