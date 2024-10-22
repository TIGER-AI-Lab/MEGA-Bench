# Task: Photo sharing image retrieval

## Task Description:

```
During a dialogue between two users, a user shares a photo during the conversation. Your task is to understand the dialogue context and retrieve the photo from the ten candidate images. You need to provide the index of the photo, which is an integer starting from 1.
```

![Image](0.png)

![Image](1.png)

![Image](2.png)

![Image](3.png)

![Image](4.png)

![Image](15.png)

![Image](20.png)

![Image](32.png)

![Image](43.png)

![Image](55.png)

![Image](56.png)

![Image](57.png)

![Image](58.png)

![Image](59.png)

![Image](60.png)

## The 1-shot Example for Task Demonstration:

## Example Query:

```
Question: [{'message': 'What are you up too?', 'user_id': 1},
 {'message': 'Just relaxing at home and you?', 'user_id': 0},
 {'message': "Just finishing up some laundry I didn't get to yesterday!",
  'user_id': 1},
 {'message': 'Nice!', 'user_id': 0},
 {'message': 'yes! one of those boring adult chores.', 'user_id': 1},
 {'message': 'I actually got to spend some time with my dad recently which was nice',
  'user_id': 0},
 {'message': 'Oh how nice! What did you guys do??', 'user_id': 1},
 {'message': 'We took him to get a much needed haircut haha', 'user_id': 0},
 {'message': 'Quarantine do a number on his hair hahaha', 'user_id': 1},
 {'message': 'exactly', 'user_id': 0},
 {'message': "Well I'm sure it looks great!", 'user_id': 1},
 {'message': '[SHARE PHOTO]', 'user_id': 0},
 {'message': 'This was where we got it', 'user_id': 0},
 {'message': 'can you see?', 'user_id': 0},
 {'message': 'Oh did you do it yourself?!', 'user_id': 1},
 {'message': 'Yes! looks good!', 'user_id': 1},
 {'message': 'Haha yep! It was fun', 'user_id': 0},
 {'message': 'Well I have to run, but good catching up', 'user_id': 0},
 {'message': 'Yes same to you! Hope to talk soon!', 'user_id': 1},
 {'message': 'bye!', 'user_id': 0}]
```

```
Demonstration example(s) of the task:
Example 1:
Example Question: [{'message': 'How are you?', 'user_id': 1},
 {'message': "I'm good. I just got back from the grand reopening of a resort in Vegas.",
  'user_id': 0},
 {'message': 'whoa', 'user_id': 1},
 {'message': 'We had fun. We had drinks and gambled and danced all night.',
  'user_id': 0},
 {'message': 'oh..so you had a great time?', 'user_id': 1},
 {'message': 'with friends or with family?', 'user_id': 1},
 {'message': 'It was awesome! The building is amazing with neat lighting and architecture.',
  'user_id': 0},
 {'message': 'I went with my boyfriend.', 'user_id': 0},
 {'message': 'oh', 'user_id': 1},
 {'message': 'okay', 'user_id': 1},
 {'message': "Here's a pic//", 'user_id': 0},
 {'message': '[SHARE PHOTO]', 'user_id': 0},
 {'message': 'hey interesting', 'user_id': 1},
 {'message': 'Yeah. Have you ever been to Vegas?', 'user_id': 0},
 {'message': 'no i am not', 'user_id': 1},
 {'message': 'You should go sometime if you can. As you can see, the service is amazing, and the buildings are huge.',
  'user_id': 0},
 {'message': 'sure', 'user_id': 1},
 {'message': 'big resort huh?', 'user_id': 1},
 {'message': 'ok bye gotta go', 'user_id': 1}]
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1489
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Diagram
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'index': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'index': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were from the PhotoChat dataset. Questions and answers are designed by the annotator
