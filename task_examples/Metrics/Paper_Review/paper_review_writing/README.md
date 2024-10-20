# Task: paper_review_writing

## Task Description:

```
Based on the given paper screenshot and the name of an artificial intelligence conference, simulate a human reviewer and write a review.

This task requires the model to:

Analyze the content of the paper from the provided screenshot
Consider the standards and expectations of the specified AI conference
Evaluate various aspects of the paper, such as:
Novelty and originality of the research
Methodology and technical soundness
Clarity of presentation
Experimental results and their interpretation
Potential impact on the field
Relevance to the conference themes
Compose a review that:
Summarizes the paper's main contributions
Highlights strengths and weaknesses
Provides constructive criticism
Suggests potential improvements
Reflects the writing style and tone typical of academic peer reviews
Include specific elements common in conference reviews, such as:
An overall assessment
Detailed comments on different sections of the paper
Questions or concerns for the authors to address
A recommendation regarding acceptance (if appropriate for the conference format)
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](Screenshot_2024-09-08_at_16.53.38.png)

![Image](Screenshot_2024-09-08_at_16.53.50.png)

![Image](Screenshot_2024-09-08_at_16.54.12.png)

![Image](Screenshot_2024-09-08_at_16.54.31.png)

```
Example Question: The conference is ICLR.
Example Response: Answer: **Summary:**

The paper proposes a statistical test that given certain assumptions can indicate whether a black-box language model has been trained on certain datasets. This is a topic of increasing interest and importance given the prevalence of pretrained models that are trained on very large amounts of data. The authors first propose a simple permutation test and identify some weaknesses with it. They then propose a more sophisticated sharded test. The authors show 2 kinds of experiments:

(1) They test on a dataset where they have injected a small amount of certain test sets to see if their approach can detect them.

(2) They apply their test to existing models such as Lllama-2 showing their approach can scale.

**Soundness:** 3 good

**Presentation:** 3 good

**Contribution:** 3 good

**Strengths:**

-Topic of large importance in the community given the direction of the field.

-Novel approach with thorough empirical results. I have some questions about the definition of test set contamination below.

-Well written and interesting.

**Weaknesses:**

I have some questions about the definition of test set contamination below.

**Questions:**

In Figure 1 the authors show test set contamination for BoolQ. But the examples there are unlabeled. Are the authors targeting unlabeled test set contamination i.e. the input is present in the pretraining data but not the label?

Would be great to have some justification and explanation of this setting.

**Flag For Ethics Review:** No ethics review needed.

**Rating:** 8: accept, good paper

**Confidence:** 3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**Code Of Conduct:** Yes
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 738
- **Eval Context**: {}
- **Taxonomy Tree Path**: Metrics;Paper_Review
- **App**: Metrics
- **Input Format**: Text-Based Images and Documents
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
