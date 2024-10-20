# Task: booking_web_rating

## Task Description:

```
Given a set of screenshots taken from a booking website, each query will ask about a random place name. You need to find the queried place in the images and answer how many people give the reviews and what is the overall rate of this place.
```

![Image](433.png)

![Image](434.png)

![Image](435.png)

![Image](436.png)

![Image](437.png)

![Image](438.png)

![Image](439.png)

![Image](441.png)

![Image](442.png)

![Image](web-1.png)

![Image](web-2.png)

![Image](web-3.png)

![Image](web-4.png)

![Image](web-5.png)

![Image](web-6.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
Example Question: West Best Pizza Company
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'number of reviews': '118', 'rating score': '3.0 stars'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4298
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Structured_Parsing
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'number of reviews': 'exact_str_match', 'rating score': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'number of reviews': 1, 'rating score': 1}}
  - **Response Parse Function**: json
