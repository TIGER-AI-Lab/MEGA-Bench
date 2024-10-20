# Task: GUI_Act_Web_Multi

## Task Description:

```
Your tasks involves interacting with web interfaces to find information about various topics. Given a question, you will be asked to perform an action on a web interface. The action can be clicking on a button, hovering over an element. You will be provided with an image of the web interface and the question. You need to give the correct action and the position of the element on which the action is performed. The action includes click and hover. The position is represented as a bounding box in the format <box>top_left_x, top_left_y, bottom_right_x, bottom_right_y</box>. The position box is normalized to the image size.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](uid_record_03567_step_00.png)

```
Example Question: 有没有关于《黑子的篮球》的新剧场版的消息？
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'Action': 'hover', 'Position Box': '<box>0.734, 0.292, 0.792, 0.328</box>'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3720
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning;GUI_Operation
- **App**: Planning
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Action': 'exact_str_match', 'Position Box': 'xml_nbbox_iou_single'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Action': 1, 'Position Box': 1}}
  - **Response Parse Function**: json
