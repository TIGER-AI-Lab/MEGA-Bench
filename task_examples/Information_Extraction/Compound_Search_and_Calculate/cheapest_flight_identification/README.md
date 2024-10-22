# Task: Cheapest flight identification

## Task Description:

```
Given a screenshot from a flight booking webpage, identify the flight number of the cheapest available flight.  If there are multiple flights with the same lowest price, output the flight numbers in the order they appear in the image from top to bottom, and separate the flight numbers with "OR" (e.g., "AA123 OR BA456").  If the cheapest flight includes connecting flights, separate the flight numbers with "and" (e.g., "AA123 and BA456").  If there are multiple sets of connecting flights with the same lowest price, separate the flight numbers in each set with "and" and separate each set with "OR" (e.g., "AA123 and BA456 OR CD789 and EF012").
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](cheapest_flight_identification1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: DL 5819 and DL 5233
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1550
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Compound_Search_and_Calculate
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Screenshots were taken by the human annotator on [Google Flights](https://www.google.com/travel/flights). Questions and answers were created by the annotator.
