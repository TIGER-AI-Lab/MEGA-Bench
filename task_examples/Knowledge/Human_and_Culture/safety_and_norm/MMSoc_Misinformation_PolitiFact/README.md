# Task: Mmsoc misinformation politifact

## Task Description:

```
You will be given an image and some text about politics, your task is to figure out whether there is mininformation. The answer should follow the format "Answer: $BOOL". $BOOL is 1 if you think the image contains misinformation, $BOOL is 0 otherwise.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: Inside a Fake News Sausage Factory: ‘This Is All About Income’ In Tbilisi, the two-room rented apartment Mr. Latsabidze shares with his younger brother is an unlikely offshore outpost of America’s fake news industry. The two brothers, both computer experts, get help from a third young Georgian, an architect. They say they have no keen interest in politics themselves and initially placed bets across the American political spectrum and experimented with show business news, too. They set up a pro-Clinton website, walkwithher.com, a Facebook page cheering Bernie Sanders and a web digest of straightforward political news plagiarized from The New York Times and other mainstream news media. But those sites, among the more than a dozen registered by Mr. Latsabidze, were busts. Then he shifted all his energy to Mr. Trump. His flagship pro-Trump website, departed.co, gained remarkable traction in a crowded field in the prelude to the Nov. 8 election thanks to steady menu of relentlessly pro-Trump and anti-Clinton stories. (On Wednesday, a few hours after The New York Times met with Mr. Latsabidze to ask him about his activities, the site vanished along with his Facebook page.) “My audience likes Trump,” he said. “I don’t want to write bad things about Trump. If I write fake stories about Trump, I lose my audience.” Some of his Trump stories are true, some are highly slanted and others are totally false, like one this summer reporting that “the Mexican government announced they will close their borders to Americans in the event that Donald Trump is elected President of the United States.” Data compiled by Buzzfeed showed that the story was the third most-trafficked fake story on Facebook from May to July. So successful was the formula that others in Georgia and other faraway lands joined in, too, including Nika Kurdadze, a college acquaintance of Mr. Latsabidze’s who set up his own pro-Trump site, newsbreakshere.com. Its recent offerings included a fake report headlined: “Stop it Liberals…Hillary Lost the Popular Vote by Several Million. Here’s Why.” That story, like most of Mr. Latsabidze’s work, was pilfered from the web. Mr. Latsabidze initially ran into no problems from all his cutting and pasting of other people’s stories, and he even got ripped off himself when a rival in India hijacked a pro-Trump Facebook page he had set up to drive traffic to his websites. (He said that the Indian rival had offered $10,000 to buy the page, but that he had reneged on payment after being provided with access rights and commandeered it for himself.)
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5051
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Knowledge;Human_and_Culture;safety_and_norm
- **Application**: Knowledge
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images and labels come from the MMSoc benchmark. Questions and answers were adapted by a human annotator.
