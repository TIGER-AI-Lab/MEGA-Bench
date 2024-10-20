# Task: music_info_retrieval

## Task Description:

```
Given a set of screenshots from an online music webpage and a specific query, retrieve the names  of the songs that match the query.  If there are multiple matching songs, provide a list of song names separatede by comma
```

![Image](music_info_retrieval1.png)

![Image](music_info_retrieval2.png)

![Image](music_info_retrieval3.png)

![Image](music_info_retrieval4.png)

![Image](music_info_retrieval5.png)

![Image](music_info_retrieval6.png)

![Image](music_info_retrieval7.png)

![Image](music_info_retrieval8.png)

![Image](music_info_retrieval9.png)

![Image](music_info_retrieval10.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
Example Question: Find the song with the longest duration.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Still Got The Blues
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 883
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Search_by_Attribute_wo_Calculate
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'answer': 'str_set_equality_comma'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'answer': 1}}
  - **Response Parse Function**: answer_string
