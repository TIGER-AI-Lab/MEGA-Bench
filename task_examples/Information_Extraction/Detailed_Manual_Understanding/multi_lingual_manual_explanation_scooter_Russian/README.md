# Task: Multi lingual manual explanation scooter russian

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

## Example Query:

```
Question: Я встал на самокат и нажал на кнопку, но самокат не двигается. Аккумулятор заряжен, и неисправностей нет. В чем может быть проблема?
```

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

## Additional Information:

- **Sample ID**: 849
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Detailed_Manual_Understanding
- **Application**: Information_Extraction
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Screenshots taken from user manual located at [https://fcc.report/FCC-ID/2A33E5LCHG11U/6288539.pdf](https://fcc.report/FCC-ID/2A33E5LCHG11U/6288539.pdf). Questions and answers created by human annnotator.
