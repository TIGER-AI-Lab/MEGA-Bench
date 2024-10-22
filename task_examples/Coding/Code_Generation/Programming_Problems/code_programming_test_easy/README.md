# Task: Code programming test easy

## Task Description:

```
Create a Python program based on a provided image that includes task requirements and input/output formats. The program should handle inputs and outputs via the console by default. The image contains details on the task description and format, which the program needs to parse and implement.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](01.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: input_data = input()

float1, integer, char, float2 = input_data.split()

float1 = float(float1)
integer = int(integer)
float2 = float(float2)

print(f"{char} {integer} {float1:.2f} {float2:.2f}")
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1373
- **Eval Context (for this query sample)**: {'test_case': {'input': ['21:11'], 'expected': '9:11 PM'}}
- **Taxonomy Tree Path**: Coding;Code_Generation;Programming_Problems
- **Application**: Coding
- **Input Format**: Text-Based Images and Documents
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'answer': 'program_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data and test cases are collected from [Pintia](https://pintia.cn)
