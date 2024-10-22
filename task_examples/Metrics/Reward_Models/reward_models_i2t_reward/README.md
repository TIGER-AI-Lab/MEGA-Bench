# Task: Reward models i2t reward

## Task Description:

```
Given an image, a question, and a pair of responses, you need to rate which one is better. You need to output "response 1" or "response 2".
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](image1.png)

```
Example Question: Question: Who is more likely to use these tools a leather crafter or a paper crafter?
Response 1: A leather crafter is more likely to use these tools. The image shows various crafting tools, including scissors and a hole punch, which are commonly used in leatherworking projects. Leather is a material that requires cutting, shaping, and precise hole-punching techniques to create desired designs or patterns. In contrast, paper crafters typically use different types of tools, such as adhesives, decorative papers, or specialized cutting machines like the Silhouette Cameo, for their projects.
Response 2: A leather crafter is more likely to use these tools as they consist of a hole punch, scissors, and a knife. These items are typically used in crafting projects involving fabric or leather materials for various designs and patterns. Paper crafters may also benefit from some of these tools, but their primary focus would be on paper-related projects, which might require different types of tools such as paper cutters or scrapbooking supplies.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: response 1
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 6419
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Metrics;Reward_Models
- **Application**: Metrics
- **Input Format**: Photographs
- **Output Format**: exact_text
- **Metric Info**:
  - **Field Score Function**: {'chosen': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'chosen': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were collected from RLAIF-V dataset. Questions and answers were adapted by the annotator
