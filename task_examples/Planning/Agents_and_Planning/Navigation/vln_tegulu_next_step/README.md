# Task: vln_tegulu_next_step

## Task Description:

```
You are a navigation agent. You are provided with a long navigation instruction in telugu and several images.

The first 4 images are taken at the current location from 4 different directions. Images starting from the image 5 are taken at different adjacent locations of the current location. Please choose which image is from the next step of the current location based on the navigation instruction. Output should follow the format of "Answer: image X ".
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](f7ef3082a05c40659421f0a21731ae1b_skybox1_sami.png)

![Image](f7ef3082a05c40659421f0a21731ae1b_skybox2_sami.png)

![Image](f7ef3082a05c40659421f0a21731ae1b_skybox3_sami.png)

![Image](f7ef3082a05c40659421f0a21731ae1b_skybox4_sami.png)

![Image](1_1_gt.png)

![Image](1_2.png)

![Image](1_3.png)

```
Example Question: ఇప్పుడు మీరు పూల మొక్కల పక్కన ఉన్నారు. కుడివైపు తిరిగి మీ ఎదురుగా తెరిచి ఉన్న తలుపు లోపలికి వెళ్ళండి. మీ కుడివైపున ఒక స్థంభం ఉంది. ఆ స్థంభంను దాటుతూ మముందుకు నడవండి. ఇప్పుడు మీ కుడివైపున భోజన బల్ల ఉంది. మీ ఎదురుగా ఉన్న దారిలో నడుస్తూ వెళ్ళండి. అలాగే మముందుకు వెళ్ళ. మీ ఎదురుగా బల్ల మరియర్చీలు ఉన్నాయి. కుడివైపున ఆ బల్లను దాటుతూ మముందుకు నడవండి. ఇక్కడి ననుండి కుడివైపు తిరిగి మీ మముందు ఉన్న దారిలో నడవండి. ఇప్పుడు మీ కుడివైపున కాస్త దూరంలో పొయ్యి ఉంది. మీ ఎదురుగా తెరిచి ఉన్న తలుపు లోపలికి వెళ్లి ఆగండి. ఈ గదిలో ఆరాలో కొన్ని వస్తువులు ఉనన్
నాయి. ఇక్కడే ఆగం.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: image 5
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3191
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning;Navigation
- **App**: Planning
- **Input Format**: Photographs
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'next step': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'next step': 1}}
  - **Response Parse Function**: answer_string
