# Task: newspaper_ocr_in_query_box

## Task Description:

```
Given a newspaper page and a bounding box query specifying the location of a section in the page, please answer the section title. The bounding box is in the format of (x1,y1,x2,y2), where (x1,y1) and (x2,y2) are the top-left and right-bottom corner. The coordinates are normalized by the image's height and width. Ignore all punctuation and newline characters; only show the words.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](109.png)

```
Example Question: The section bounding box is (0.0,0.05,0.27,0.61)
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: BOYD AND HAMILTON BACK FROM SERVICE IN FRANCE
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1238
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Document;Document_Info_Parsing
- **App**: Perception
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'section title': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'section title': 1}}
  - **Response Parse Function**: answer_string
