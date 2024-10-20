# Task: media_homepage_profile

## Task Description:

```
Given a set of screenshots taken from various homepages, each query will ask about one research interest. You need to find out who works in this area and then output the person's name and affiliation (university or company). The answer should be a list of tuple, with format "Answer: [('name', 'affiliation'), ...] ". The answer text should directly come from the image. Each person's name and corresponding affiliation should be paired. If the person is moving, use the latest affiliation. Do not include abbreviation of names or any other unnecessary outputs.
```

![Image](12.png)

![Image](11.png)

![Image](10.png)

![Image](14.png)

![Image](13.png)

![Image](15.png)

![Image](16.png)

![Image](17.png)

![Image](18.png)

![Image](9.png)

![Image](web-1.png)

![Image](web-2.png)

![Image](web-3.png)

![Image](web-4.png)

![Image](web-5.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
Example Question: electronic engineering
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: [('Yuan Cao', 'Harvard University')]
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3639
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Search_by_Attribute_wo_Calculate
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'jaccard_index_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
