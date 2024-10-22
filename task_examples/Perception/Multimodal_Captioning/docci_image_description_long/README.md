# Task: Docci image description long

## Task Description:

```
You are a multi-modal AI assistant, now look at the image carefully, writing down a detailed caption about the given that captures all necessary visual details.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](qual_dev_00006.png)

```
Example Response: Answer: A side view of a Red Ferrari 812 Superfast parked in an indoor display with a metal information sign to the left of the front driver side tire. The Ferrari is facing to the left. The ferrari is parked on beige rectangular tiles with a row of headlights casting light onto the tiles. The wall behind the Ferrari has a large mounted image of a red Formula 1 car with Shell oil company livery displaying the number "16" on a race track. There is a single metal door at the right of the frame.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Information:

- **Sample ID**: 724
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Multimodal_Captioning
- **Application**: Perception
- **Input Format**: Photographs
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data were collected from DOCCI
