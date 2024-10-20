# Task: ocr_table_to_html

## Task Description:

```
You are given an image of a table. You need to convert this to the simplest html format like
ˋˋˋ
<table>
...
</table>
ˋˋˋ
No need to use <thead>, and ignore all the formatting requirements like color, background, font, etc.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](Figure1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: <table>
  <tr>
    <th>Name</th>
    <th>School</th>
    <th>Gender</th>
    <th>Weight</th>
    <th>Height</th>
  </tr>
  <tr>
    <td>Kim</td>
    <td>UCB</td>
    <td>Male</td>
    <td>52kg</td>
    <td>168cm</td>
  </tr>
  <tr>
    <td>Mariton</td>
    <td>Stanford</td>
    <td>Female</td>
    <td>43kg</td>
    <td>159cm</td>
  </tr>
  <tr>
    <td>George</td>
    <td>UCSB</td>
    <td>Male</td>
    <td>54kg</td>
    <td>172cm</td>
  </tr>
</table>
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 6107
- **Eval Context**: {}
- **Taxonomy Tree Path**: Coding;Code_Generation;Document_Conversion
- **App**: Coding
- **Input Format**: Text-Based Images and Documents
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'output': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'output': 1}}
  - **Response Parse Function**: answer_string
