# Task: Signage navigation

## Task Description:

```
Given a query image of signages in airports, railway stations, etc., your task is to answer the navigation-related question.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: I want to go to Exit 1. Which direction should I go? Please choose from ['Straight ahead', 'Turn left', 'Turn right'].
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Turn left
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3291
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge
- **Application**: Knowledge
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images come from various websites. Questions and answers were created by a human annotator.
