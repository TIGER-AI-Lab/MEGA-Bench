# Task: video_intent_recognition

## Task Description:

```
Provide a video clip along with a transcript of the speaker's words. Your task is to identify the speaker's intent. Possible choices include: Complain, Praise, Apologize, Thank, Criticize, Care, Agree, Taunt, Flaunt, Oppose, Joke, Inform, Advise, Arrange, Introduce, Comfort, Leave, Prevent, Greet, Ask for help. Make sure your answer is one of them.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

[Please watch the local video: 1.mp4]

```
Example Question: god, i can't take it!
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Complain
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3706
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;Human_and_Culture;emotion_and_intent_understanding
- **App**: Knowledge
- **Input Format**: Videos
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
