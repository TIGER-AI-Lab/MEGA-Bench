# Task: Flowchart code generation

## Task Description:

```
You will be presented with a flowchart and multiple Python code snippets. Your task is to carefully examine the flowchart and each of the provided code snippets, then select the code snippet that most accurately mirrors the flowchart’s logic and structure.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: Which of the following code snippets best describes the flowchart?

A) ˋˋˋpython
if not lamp_plugged_in:
    plug_in_lamp()
elif bulb_burned_out:
    replace_bulb()
else:
    repair_lamp()
ˋˋˋ

B) ˋˋˋpython
if lamp_plugged_in:
    if bulb_burned_out:
        replace_bulb()
    else:
        repair_lamp()
else:
    plug_in_lamp()
ˋˋˋ

C) ˋˋˋpython
if lamp_plugged_in:
    repair_lamp()
else:
    if bulb_burned_out:
        replace_bulb()
    else:
        plug_in_lamp()
ˋˋˋ

D) ˋˋˋpython
if bulb_burned_out:
    replace_bulb()
elif not lamp_plugged_in:
    plug_in_lamp()
else:
    repair_lamp()
ˋˋˋ
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: B
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 2593
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Coding;Code_Understanding;Code_Match
- **Application**: Coding
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data are collected from website, and the question and answer are designed by human annotator
