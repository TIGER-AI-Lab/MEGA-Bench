# Task: multi_lingual_manual_explanation_scooter_Russian

## Task Description:

```
На основе предоставленных изображений из руководства пользователя, ответьте на вопросы на русском языке. Для вопросов, связанных с эксплуатацией, предоставьте решения. Для вопросов, касающихся безопасности, дайте разумные рекомендации.
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
Example Question: У этого самоката есть функция освещения? Если да, то как её включить?
Example Response: Answer: Да, самокат оснащён LED-освещением. Вы можете включить или выключить его, следуя следующим шагам:

​	1.	Убедитесь, что самокат включён: нажмите кнопку питания, чтобы активировать самокат.

​	2.	Включение освещения: когда самокат включён, коротко нажмите кнопку питания один раз, чтобы включить передний LED-фонарь.

​	3.	Выключение освещения: повторно коротко нажмите кнопку питания, чтобы выключить LED-фонарь.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 849
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Detailed_Manual_Understanding
- **App**: Information_Extraction
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
