# Task: tv_show_retrieval_by_character

## Task Description:

```
Given a set of screenshots from a TV show website and the names of the characters depicted in those screenshots, retrieve the name of the TV shows in which those character appear.  If an character appears in multiple TV shows, list all corresponding TV shows names in a sequence format separated by comma.
```

![Image](TV_show_retrieval_by_character1.png)

![Image](TV_show_retrieval_by_character2.png)

![Image](TV_show_retrieval_by_character3.png)

![Image](TV_show_retrieval_by_character4.png)

![Image](TV_show_retrieval_by_character5.png)

![Image](TV_show_retrieval_by_character6.png)

![Image](TV_show_retrieval_by_character7.png)

![Image](TV_show_retrieval_by_character8.png)

![Image](TV_show_retrieval_by_character9.png)

![Image](TV_show_retrieval_by_character10.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
Example Question: Character Name: Flynne Fisher
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: The Peripheral
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4425
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Search_by_Attribute_wo_Calculate
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'TV_show': 'str_set_equality_comma'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'TV_show': 1}}
  - **Response Parse Function**: answer_string
