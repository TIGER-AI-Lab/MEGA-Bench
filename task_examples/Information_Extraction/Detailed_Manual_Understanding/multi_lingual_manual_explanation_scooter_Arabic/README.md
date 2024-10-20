# Task: multi_lingual_manual_explanation_scooter_Arabic

## Task Description:

```
استنادًا إلى محتوى صورة دليل المستخدم المقدم، أجب عن الأسئلة باستخدام اللغة العربية. في حال كانت الأسئلة تتعلق بمشاكل تشغيلية، قدم حلولًا. وإذا كانت الأسئلة تتعلق بسلامة الأشخاص، قدم نصائح معقولة.
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

```
Demonstration example(s) of the task:
Example 1:
Example Question: هل يحتوي السكوتر على وظيفة الإضاءة؟ وإذا كان كذلك، كيف يمكن تشغيلها؟
Example Response: Answer: نعم، السكوتر مزود بوظيفة إضاءة LED، ويمكنك تشغيلها أو إيقافها باتباع الخطوات التالية:

1. تأكد من تشغيل السكوتر: اضغط على زر الطاقة لتشغيل السكوتر.
2. تشغيل ضوء الإضاءة: عندما يكون السكوتر في وضع التشغيل، اضغط على زر الطاقة مرة واحدة بشكل قصير لتشغيل ضوء LED الأمامي.
3. إيقاف ضوء الإضاءة: اضغط مرة أخرى على زر الطاقة بشكل قصير لإيقاف ضوء LED.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 835
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Detailed_Manual_Understanding
- **App**: Information_Extraction
- **Input Format**: Text-Based Images and Documents
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
