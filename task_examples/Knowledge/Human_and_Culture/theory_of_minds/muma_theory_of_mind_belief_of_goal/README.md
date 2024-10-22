# Task: Muma theory of mind belief of goal

## Task Description:

```
You will see 20 frames from a video, in chronological order. Please answer the question based on the image frames.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1_0.png)

![Image](1_1.png)

![Image](1_2.png)

![Image](1_3.png)

![Image](1_4.png)

![Image](1_5.png)

![Image](1_6.png)

![Image](1_7.png)

![Image](1_8.png)

![Image](1_9.png)

![Image](1_10.png)

![Image](1_11.png)

![Image](1_12.png)

![Image](1_13.png)

![Image](1_14.png)

![Image](1_15.png)

![Image](1_16.png)

![Image](1_17.png)

![Image](1_18.png)

![Image](1_19.png)

```
Example Question: Given the above interaction, if Kevin has been trying to help Jessica achieve her goal, which of the following statements is MOST likely true?

When giving information, Kevin believed that there was a remote control in the kitchen cabinet
When giving information, Kevin believed that there was a spoon on the coffee table in the living room
When giving information, Kevin believed that there was a remote control on the coffee table in the living room
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: When giving information, Kevin believed that there was a remote control on the coffee table in the living room
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 982
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;Human_and_Culture;theory_of_minds
- **Application**: Knowledge
- **Input Format**: Videos
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images and labels come from the MuMA-ToM dataset . Questions and answers were adapted by a human annotator.
