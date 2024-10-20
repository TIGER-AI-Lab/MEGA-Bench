# Task: app_layout_understanding_twitter

## Task Description:

```
The image below is a screenshot of the Twitter interface. From the following options, identify the feature highlighted by the red box in the image: [Respond to tweets with my thoughts, Share others' posts to my followers, Show appreciation for tweets, Save posts for later viewing, Check my recent interactions, Access premium features, Share my own message or media, Read private conversations, View my Twitter presence, See accounts I follow, I want to know how popular this post is and how many people have seen it, my friends on Telegram should be very interested in this post, try out the recently popular Grok 2, check my community, I want to see the recent trends].
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](WX20240802-214043@2x.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Respond to tweets with my thoughts
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5781
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;App_Function_Understanding
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
