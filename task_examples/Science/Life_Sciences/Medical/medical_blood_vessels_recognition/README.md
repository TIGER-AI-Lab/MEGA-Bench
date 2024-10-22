# Task: Medical blood vessels recognition

## Task Description:

```
Given the medical image of blood vessels, you are asked to answer: 1. what's the type of the query image. The answer should be from (CT, Fundus Photography, Infrared Reflectance (IR) imaging, MRI, OCT, UltraSound); 2. describe which part is illustrated in the (highlight) area of the query image. The answer should be from (ascending aorta, iliac artery, renal artery, retinal artery, retinal vessel, portal vein, inferior vena cava).
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1986.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'Type': 'MRI', 'Answer': 'ascending aorta'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 2419
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Science;Life_Sciences;Medical
- **Application**: Science
- **Input Format**: Text-Based Images and Documents
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Type': 'exact_str_match', 'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Type': 1, 'Answer': 1}}
  - **Response Parse Function**: json
- **Source Description**: Data collected from GMAI-MMBench, and the questions and answers are adapted to match strings
