# Task: multilingual_news_qa

## Task Description:

```
There are several soccer news posts from social media in English. Given a question in Chinese, you need to first find the relevant news and then use the exact words from the news to answer if possible. The answer should be as simple as possible.
```

![Image](Screenshot_2024-09-05_at_11.00.14_PM.png)

![Image](Screenshot_2024-09-05_at_11.02.43_PM.png)

![Image](Screenshot_2024-09-05_at_11.04.09_PM.png)

![Image](Screenshot_2024-09-05_at_11.05.18_PM.png)

![Image](Screenshot_2024-09-05_at_11.06.12_PM.png)

![Image](Screenshot_2024-09-05_at_11.06.46_PM.png)

![Image](Screenshot_2024-09-05_at_11.07.41_PM.png)

![Image](Screenshot_2024-09-05_at_11.07.56_PM.png)

![Image](Screenshot_2024-09-05_at_11.08.08_PM.png)

![Image](Screenshot_2024-09-05_at_11.09.13_PM.png)

![Image](Screenshot_2024-09-05_at_11.09.40_PM.png)

![Image](Screenshot_2024-09-05_at_11.10.04_PM.png)

![Image](Screenshot_2024-09-05_at_11.10.30_PM.png)

![Image](Screenshot_2024-09-05_at_11.12.18_PM.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
Example Question: 对阵皇家社会的比赛，安切洛蒂计划让谁出任中卫？
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Tchouaméni
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3475
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Multimodal_QA
- **App**: Information_Extraction
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'multi_ref_phrase'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
