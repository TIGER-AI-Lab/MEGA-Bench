# Task: booking_web_recommendation

## Task Description:

```
Given a set of screenshots taken from a booking website, each query will ask about a random time slot. You need to recommend the suitable restaurants that are open during that period. The answer should be a list in the format of ["restaurants1", "restaurants2", ...]
```

![Image](433.png)

![Image](434.png)

![Image](435.png)

![Image](436.png)

![Image](437.png)

![Image](439.png)

![Image](440.png)

![Image](441.png)

![Image](web-1.png)

![Image](web-2.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
Example Question: 6:00 am - 9:00 am Tuesday
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: ["Mcdonald's", "Lewis Babies Cookies and More", "Primo Burgers"]
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3561
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Search_by_Attribute_wo_Calculate
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'restaurants': 'jaccard_index_case_insensitive'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'restaurants': 1}}
  - **Response Parse Function**: answer_string
