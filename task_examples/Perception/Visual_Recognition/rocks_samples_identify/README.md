# Task: rocks_samples_identify

## Task Description:

```
Imagine you are a college student studying geology. Given some pictures of rocks, please identify what kind of rock it is. Note that you need to choose from the following options: {'流纹岩/Rhyolite', '石英砂岩/Quartz sandstone', '斜长石/Plagioclase', '片岩/Schist', '板岩/Slate', '大理岩/Marble', '花岗岩/granite', '玄武岩/Basalt', '油页岩/Oil Shale', '石英岩/Quartzite', '凝灰岩/Tuff', '蛇纹岩/Serpentinite', '橄榄岩/Peridotite', '绿泥石片岩/Chlorite schist', '浮岩/Pumice', '珍珠岩/Perlite', '砂岩/sandstone', '千枚岩/Phyllite', '岩屑砂岩/Lithic sandstone', '正长岩/Syenite', '闪长岩/Diorite', '片麻岩/Gneiss', '硬石膏/Anhydrite', '黑曜岩/Obsidian', '安山岩/Andesite', '砾岩或角砾岩/Conglomerate or breccia', '煤或燧石/Coal or Flint', '斜长角闪岩/Amphibolite'}.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](000.png)

![Image](001.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 千枚岩/Phyllite
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 4524
- **Eval Context**: {}
- **Taxonomy Tree Path**: Perception;Visual_Recognition
- **App**: Perception
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
