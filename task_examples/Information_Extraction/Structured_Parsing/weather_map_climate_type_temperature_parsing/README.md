# Task: Weather map climate type temperature parsing

## Task Description:

```
Given a query weather map and a city in this image, you are asked to indicate the weather phenomenon and temperature near the given city in example question. The weather types should be selected from (sunny, rainy, cloudy, thunderstorm, snowy). Please also include the temperature unit that is either Fahrenheit or Celsius based on the specific image.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](302.png)

```
Example Question: San Fransisco
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'weather': 'sunny', 'temperature': '75 Fahrenheit'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3126
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Structured_Parsing
- **Application**: Information_Extraction
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'weather': 'exact_str_match', 'temperature': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'weather': 1, 'temperature': 1}}
  - **Response Parse Function**: json
- **Source Description**: One of the examples comes from the SEED-Bench 2 Plus benchmark . The rest of the images were collected from various online websites. Questions and annotations were adapted by a human annotator.
