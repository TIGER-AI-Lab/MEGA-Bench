# Task: Multi lingual manual explanation scooter chinese

## Task Description:

```
根据给定的用户手册图片内容，使用中文回答问题。涉及操作上的问题，给出解决方法。涉及人身安全上的问题给出合理建议。
```

![Image](1.png)

![Image](2.png)

![Image](3.png)

![Image](4.png)

![Image](5.png)

![Image](6.png)

![Image](7.png)

![Image](8.png)

## The 1-shot Example for Task Demonstration:

## Example Query:

```
Question: 我站上滑板车，按下开关后滑板车不动，电是满的并且车没有故障，什么情况？
```

```
Demonstration example(s) of the task:
Example 1:
Example Question: 这个车有照明功能嘛？有的话该如何开启
Example Response: Answer: 是的，滑板车配有LED照明功能，您可以通过以下步骤来开启或关闭：
​	1.	确保滑板车开启：按下电源按钮，打开滑板车。

​	2.	开启照明灯：在滑板车启动状态下，短按电源按钮一次，即可开启前置LED照明灯。

​	3.	关闭照明灯：再次短按电源按钮，即可关闭LED照明灯。
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Information:

- **Sample ID**: 891
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Detailed_Manual_Understanding
- **Application**: Information_Extraction
- **Input Format**: Text-Based Images and Documents
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Screenshots taken from user manual located at [https://fcc.report/FCC-ID/2A33E5LCHG11U/6288539.pdf](https://fcc.report/FCC-ID/2A33E5LCHG11U/6288539.pdf). Questions and answers created by human annnotator.
