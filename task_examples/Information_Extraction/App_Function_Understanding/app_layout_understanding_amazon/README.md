# Task: App layout understanding amazon

## Task Description:

```
The image below shows a screenshot of the Amazon website. From the options listed, identify the function highlighted by the red box in the picture: ["Specify delivery location", "Adjust linguistic preferences", "Access personal retail portal", "Explore audio peripherals", "Browse culinary equipment", "Navigate digital marketplace", "Discover additional interactive entertainment gear", "Peruse affordable footwear options", "Review pending acquisitions", "Initiate customer assistance dialogue", "View more clothing products", "I want to redeem some gift cards that friends gave me for my birthday and use them to buy headsets", "My keyboard is broken and I want to replace it with a new one", "My friends birthday is coming up and I want to give her a new mouse", "I want to buy things to be shipped to Hong Kong but Im not sure which items specifically offer free shipping"].
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](WX20240803-151303@2x.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: Specify delivery location
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 5837
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;App_Function_Understanding
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Screenshots were taken by the human annotator on [Amazon](https://www.primevideo.com/). Questions and answers were created by the annotator.
