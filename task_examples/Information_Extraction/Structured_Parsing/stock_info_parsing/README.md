# Task: stock_info_parsing

## Task Description:

```
Given a screenshot of an interactive stock market chart and related details, extract the following specific information: 

(1) Company Name 
(2) Previous Close price 
(3) Open Price
(4) Bid
(5) Ask
(6) Day's Range
(7) 52 Week Range
(8) Volume
(9) Avg. Volume
(10) Market Cap (intraday)
(11) Beta (5Y Monthly)
(12) PE Ratio (TTM)
(13) EPS (TTM)
(14) Earning Date
(15) Foward Dividend & Yield
(16) Ex-Dividend Date
(17) 1y Target Est

If any of the above information is not present in the image, leave it blank.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](stock_info_parsing1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'name': 'Intel Corporation (INTC)', 'previous': '20.69', 'open': '20.50', 'bid': '20.86 x 200', 'ask': '20.90 x 200', 'day': '20.41 - 20.89', 'week': '18.84 - 51.28', 'volume': '48,178,611', 'avg': '58,302,990', 'cap': '89.24B', 'beta': '1.05', 'PE': '86.96', 'EPS': '0.24', 'earning': 'Oct 24, 2024 - Oct 28, 2024', 'yield': '0.50 (2.42%)', 'Ex': 'Aug 7, 2024', 'target': '24.44'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2012
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Structured_Parsing
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'name': 'simple_str_match', 'previous': 'simple_str_match', 'bid': 'simple_str_match', 'target': 'simple_str_match', 'open': 'simple_str_match', 'ask': 'simple_str_match', 'day': 'simple_str_match', 'week': 'simple_str_match', 'volume': 'simple_str_match', 'avg': 'simple_str_match', 'cap': 'simple_str_match', 'beta': 'simple_str_match', 'EPS': 'simple_str_match', 'earning': 'simple_str_match', 'yield': 'simple_str_match', 'Ex': 'simple_str_match', 'PE': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'name': 1, 'previous': 1, 'bid': 1, 'target': 1, 'open': 1, 'ask': 1, 'day': 1, 'week': 1, 'volume': 1, 'avg': 1, 'cap': 1, 'beta': 1, 'EPS': 1, 'earning': 1, 'yield': 1, 'Ex': 1, 'PE': 1}}
  - **Response Parse Function**: json
