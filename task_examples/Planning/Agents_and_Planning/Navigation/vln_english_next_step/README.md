# Task: Vln english next step

## Task Description:

```
You are a navigation agent. You are provided with a long navigation instruction and several images.

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
Example Question: You are in the open area facing towards the plants. Turn right and walk straightly through the open door. Now you are facing towards the glass windows. Slightly turn right and move towards the single white couch. Now turn right and walk straightly till you find a dining table in front of you. Now slightly turn right and move towards the wooden cupboards. Now turn right and walk straightly by passing the stove on your right side till you find an open door in front of you. Walk through the door and enter into the room. Now you are facing towards the white shelves which has glasses and cups on it. That will be the end point.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: image 5
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3460
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning;Navigation
- **Application**: Planning
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'next step': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'next step': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from RxR dataset, the question and answer are adapted by human annotator
