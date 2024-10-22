# Task: Iam line ocr and locate

## Task Description:

```
Given two pictures of handwriting, one for an entire page, the other for a line, you are asked to first precisely convert the line picture to the corresponding typed words, separated by "|". Then, you also need to tell the index of this line in the entire page. If the line does not exist in the page, you should answer "NA". Treat punctuation and symbols as words. Capitalization matters. Scribbled out words are labeled as the word "#".
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](a01-000u-04.png)

![Image](a01-000u.png)

```
Example Question: The first image is the line, the second image is the page.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'typed text': 'put|down|a|resolution|on|the|subject', 'line index': '5'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 1913
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Perception;Diagram_and_Document_Understanding;Document;Document_Info_Parsing
- **Application**: Perception
- **Input Format**: Text-Based Images and Documents
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'typed text': 'normalized_similarity_damerau_levenshtein', 'line index': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'typed text': 1, 'line index': 1}}
  - **Response Parse Function**: json
- **Source Description**: Images were collected from the IAM handwritten database. Questions and answers were re-designed by the annotator
