# Task: App layout understanding zoom

## Task Description:

```
Zoom is an online meeting app. The image below is a screenshot of the Zoom interface. From the following list of features, select the function indicated by the red box in the image: [Start a New Meeting, Join a Meeting, Schedule a Meeting, Share Screen, Add to Calendar, View or Edit Settings, Search for Contacts or Meetings, View or Edit Profile, View Notifications, View Past or Future Meeting Information, View meeting recordings, My client keeps crashing, I want to report the error, back in chat, I want to open the whiteboard, I want to check missed calls, I want to change the background image].
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](WX20240801-185517@2x.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Start a New Meeting
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5865
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;App_Function_Understanding
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Screenshots were taken by the human annotator on [Zoom](https://zoom.us). Questions and answers were created by the annotator.
