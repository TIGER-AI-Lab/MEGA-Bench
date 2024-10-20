# Task: clip_stable_diffusion_generate

## Task Description:

```
Your task is to determine if the image is generated by a generaive AI model based on the text description. You will be give the caption and the image. The answer should follow the format "Answer: $BOOL". $BOOL is 1 if you think the image is generated, $BOOL is 0 if you think the image is a natural image.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](54303_clip.png)

```
Example Question: A destroyed neighborhood is seen in the city of Daraya southwest of the capital Damascus as fighting between opposition forces and troops loyal to the government of Syrian President Bashar alAssad continues on Jan 12 2014
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5499
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;Fact_Checking
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string