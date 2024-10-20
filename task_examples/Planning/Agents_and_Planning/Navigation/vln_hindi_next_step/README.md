# Task: vln_hindi_next_step

## Task Description:

```
You are a navigation agent. You are provided with a long navigation instruction in hindi and several images.

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
Example Question: आपके सामने एक गमला है वहा से दाए मुड़े और सीधा चलकर भूरे रंग के खुले दरवाज़े में प्रवेश करें और हल्का सा दाए मुड़कर खम्भे को पार करते हुए दाए मुड़े। अब आपके दाए ओर एक मेज़ और सफ़ेद रंग की कुर्सिससिां                                                                                                                                           
गी वहा से सीधा चलकर सामने वाली कमान में प्रवेश करें। आपके सामने एक भूरे रंग का खाने का मेज़ होगा वो मेज़ के दाए ओर से सीधा चलते जाए और दाए मुड़े। अब आपके दाए ओर एक सफ़ेद रंग का मेज़ और क कु
छ कुर्सिसिसिां   ोंगी वहा से सीधा चलकर बाए ओर वाले तंदूर यंत्र को पार करते हुए सामने वाले भूरे रंग के रुक्जाये।ाज़े में प्रवेश करक
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: image 5
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2200
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning;Navigation
- **App**: Planning
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'next step': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'next step': 1}}
  - **Response Parse Function**: answer_string
