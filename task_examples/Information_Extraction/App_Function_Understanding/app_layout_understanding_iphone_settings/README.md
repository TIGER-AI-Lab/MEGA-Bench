# Task: app_layout_understanding_iphone_settings

## Task Description:

```
The image below is a screenshot of the Settings page on an iPhone. From the options listed, identify the function highlighted by the red box in the picture: [
    Turn off or on airplane mode,
    I've moved to a new home and want to switch my phone's Wi-Fi network,
    I bought new earphones and want to connect them to my phone,
    The Wi-Fi signal is poor, I want to use mobile data for internet access,
    My classmate is visiting and can't connect to my home Wi-Fi, so I want to use my phone to provide a hotspot for them to access the internet.,
    The notifications from various apps always disturb me, I want a quiet phone, how to set it up.,
    The ringtone and key sounds are unpleasant, I want to adjust the volume of the ringtone and key sounds,
    I'm spending too much time on my phone every day, I need to control my phone usage time to protect my eyes,
    Set up AirDrop, CarPlay, and check phone storage space,
    I want to change my phone's style from light to dark mode,
    I'm often disturbed by my phone and want to set up Do Not Disturb mode, as well as configure which apps and people can send me notifications.,
    When I swipe down from the top right corner of my phone, a page opens. I want to edit the functions on this page,
    I have many apps on my phone. Every time I download a new app, I see them. I want to set it so that when I download new apps, they're not visible on the home screen but can be found through search.,
    I want to adjust Siri's speaking speed,
    Temporarily exit settings, but don't want to close it completely because I'll need to use it again soon.
]
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](WX20240803-131130@2x.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Turn off or on airplane mode
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 5894
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;App_Function_Understanding
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
