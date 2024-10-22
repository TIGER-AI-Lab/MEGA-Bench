# Task: Doc vqa

## Task Description:

```
Read the documents shown in images and answer the questions.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1-1.png)

![Image](1-2.png)

![Image](1-3.png)

```
Example Question: What is the purpose of the Confirmation Statement mentioned in the document?
Example Response: Answer: The purpose of the Confirmation Statement is to confirm that all information required to be delivered by the company to the registrar in relation to the confirmation period concerned has been delivered or is being delivered at the same time as the confirmation statement.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Information:

- **Sample ID**: 362
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Document;Document_QA
- **Application**: Perception
- **Input Format**: Text-Based Images and Documents
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data and open-ended QA pairs were converted from DocMatix
