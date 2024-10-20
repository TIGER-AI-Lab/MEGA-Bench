# Task: movie_info_retrieval

## Task Description:

```
Given a set of screenshots from a movie website and a specific query, retrieve the names of the movies that match the query. If there are multiple matching movies, provide a sequence of movie names seperated by comma.
```

![Image](movie_info_retrieval1.png)

![Image](movie_info_retrieval2.png)

![Image](movie_info_retrieval3.png)

![Image](movie_info_retrieval4.png)

![Image](movie_info_retrieval5.png)

![Image](movie_info_retrieval6.png)

![Image](movie_info_retrieval7.png)

![Image](movie_info_retrieval8.png)

![Image](movie_info_retrieval9.png)

![Image](movie_info_retrieval10.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
Example Question: Find the movie with the highest star rating.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: The Hobbit: The Desolation of Smaug, Spaceballs
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1517
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Compound_Search_and_Calculate
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'str_set_equality_comma'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
