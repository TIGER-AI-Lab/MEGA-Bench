# Task: Video content reasoning

## Task Description:

```
Analyze the content in the given video and answer the corresponding question.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](000000.png)

![Image](000060.png)

![Image](000120.png)

![Image](000180.png)

![Image](000240.png)

![Image](000300.png)

![Image](000360.png)

![Image](000420.png)

![Image](000480.png)

```
Example Question: What are they doing in this video? Choose from "hurdle" race or "sprint".
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: hurdle race
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1698
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Summarization
- **Application**: Information_Extraction
- **Input Format**: Videos
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Videos and annotations were taken from the HME100k dataset. Questions and answers were adapted by a human annotator.
