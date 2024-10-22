# Task: Weather info retrieval

## Task Description:

```
Given a set of screenshots from a weather webpage and a specific query, retrieve the places that match the query. If there are multiple matching places, provide a list of place names separated by commas.
```

![Image](weather_info_retrieval1.png)

![Image](weather_info_retrieval2.png)

![Image](weather_info_retrieval3.png)

![Image](weather_info_retrieval4.png)

![Image](weather_info_retrieval5.png)

![Image](weather_info_retrieval6.png)

![Image](weather_info_retrieval7.png)

![Image](weather_info_retrieval8.png)

![Image](weather_info_retrieval9.png)

![Image](weather_info_retrieval10.png)

## The 1-shot Example for Task Demonstration:

## Example Query:

```
Question: Find places where the cloud cover is greater than 80%.
```

```
Demonstration example(s) of the task:
Example 1:
Example Question: Find places where the current temperature is below 20°C.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Zurich, Sydney
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1196
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Compound_Search_and_Calculate
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'str_set_equality_comma'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Screenshots were taken by the human annotator on [Microsoft Weather](https://www.msn.com/en-ca/weather/forecast). Questions and answers were created by the annotator.
