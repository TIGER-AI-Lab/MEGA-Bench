# Task: ocr_open_ended_qa

## Task Description:

```
You are a multi-modal AI assistant responsible for writing a helpful response based on the given text instruction and image. Answer in the same language as the question.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0.png)

```
Example Question: During the design challenge, there was a board displaying different materials and their corresponding quantities and weights. A photograph was taken for record-keeping. However, the image is slightly blurred and the handwriting varies in style and size. Examine the image and provide a clear and accurate transcription of the information displayed, detailing the quantities and weights of the card stock, construction paper, and fabric.
Example Response: Answer: The image shows a whiteboard with information written in marker. There are three columns, each dedicated to a different material: card stock, construction paper, and fabric. For each material, the quantity (in pieces) and the weight (in grams) are given.

Card Stock

Quantity: 3 pieces
Weight: 13 grams
Construction Paper

Quantity: 2 pieces
Weight: 6 grams
Fabric

Quantity: 32
Weight: 77 grams
The weights appear to have been underlined for emphasis. The handwriting for 'Card Stock' and 'Construction Paper' is in black ink, with the numbers also written in black. The word 'Fabric' and its corresponding numbers are written in blue ink. The font styles are casual and varied in size, but the information is nonetheless legible. The whiteboard also has a printed form at the top right corner, but the text in this form is not legible due to the angle and distance at which the photo was taken.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 246
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Object_and_Scene_Understanding
- **App**: Perception
- **Input Format**: Text-Based Images and Documents
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
