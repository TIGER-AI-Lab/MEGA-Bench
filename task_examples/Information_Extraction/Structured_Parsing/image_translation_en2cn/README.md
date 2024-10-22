# Task: Image translation en2cn

## Task Description:

```
Given a query picture, translate the English in the picture into Chinese.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 图像适配器。我们在由图像编码器生成的视觉标记表示和由语言模型生成的标记表示之间入交叉注意层（Alayrac et al., 2022）。交叉注意层在核心语言模型中每四个自注意层应用一次。与语言模型本身类似，交叉注意层使用广义查询注意（GQA）以提高效率。交叉注意层为模型引入了大量额外的可训练参数：对于Llama 3 405B，交叉注意层有≈100B参数我们在两个阶段预训练我们的图像适配器：（1）初始预训练，然后是（2）退火：

- 始预训练。我们在上述的~6B图像-文本对数据集上预训练我们的图像适配器。为了实现计效率的原因，我们将所有图像调整为最多336 x 336像素的平铺格式，其中我们将平铺排列以支持不同的纵横比，例如672 x 672、672 x 336和1344 x 336。

- 退火。我们继续在~500M张来自上述退火数据集的图像上训练图像适配器。在退火期间，我们增加每块图像的辨率，以提高在需要更高分辨率图像的任务上的性能，例如图像理解。
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3653
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Structured_Parsing
- **Application**: Information_Extraction
- **Input Format**: Text-Based Images and Documents
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'gleu_cn'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Images were collected from various sources, including academic papers, news articles, shopping receipts, etc. The annotations are obtained by GPT-4o translation followed by a human check.
