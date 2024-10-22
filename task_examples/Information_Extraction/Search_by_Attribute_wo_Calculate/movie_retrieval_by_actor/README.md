# Task: Movie retrieval by actor

## Task Description:

```
Given a set of screenshots from a movie website and the names of the actors depicted in those screenshots, retrieve the names of the movies in which those actors appear.  If an actor appears in multiple movies, list all corresponding movie names in a sequence format separated by commas.
```

![Image](Movie_retrieval_by_actor1.png)

![Image](Movie_retrieval_by_actor2.png)

![Image](Movie_retrieval_by_actor3.png)

![Image](Movie_retrieval_by_actor4.png)

![Image](Movie_retrieval_by_actor5.png)

![Image](Movie_retrieval_by_actor6.png)

![Image](Movie_retrieval_by_actor7.png)

![Image](Movie_retrieval_by_actor8.png)

![Image](Movie_retrieval_by_actor9.png)

![Image](Movie_retrieval_by_actor10.png)

## The 1-shot Example for Task Demonstration:

## Example Query:

```
Question: Actor name: Steve Carell, Timothée Chalamet
```

```
Demonstration example(s) of the task:
Example 1:
Example Question: Actor name: Nicole Wallace, Gabriel Guevara
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: My Fault
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3347
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Search_by_Attribute_wo_Calculate
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'name': 'str_set_equality_comma'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'name': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Screenshots were taken by the human annotator on the [Amazon Prime Video webpage](https://www.primevideo.com/). Questions and answers were created by the annotator.
