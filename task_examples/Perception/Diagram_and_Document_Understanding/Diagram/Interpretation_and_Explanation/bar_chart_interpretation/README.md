# Task: Bar chart interpretation

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
Example Question: What is the difference in the GDP reduction between the country with the largest decrease in economic size and the country with the eighth largest decrease?
Example Response: Answer: The image provided shows a graph with various countries and the projected change in their nominal GDP in US dollars. To answer your question, I need to identify the country with the largest GDP decrease and the country with the eighth largest decrease, then calculate the difference in the GDP reduction percentage between these two countries.

Let me analyze the image to extract the required data.
1. Russia: -$153B
2. Eygpt: -$88B
3. Canada: -$50B
4. Saudi Arabia: -$46B
5. Bangladesh: -$40B
6. Norway: -$25B
7. Kuwait: -$20B
8. Oman: -$10B

The difference between Russia and Oman's GDP reduction percentage is $153B - $10B = $143B. So, the answer is $143B.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Information:

- **Sample ID**: 289
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Diagram;Interpretation_and_Explanation
- **Application**: Perception
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: The images of bar graphs are collected from the Internet, and the annotator created the question and open-ended reference answer
