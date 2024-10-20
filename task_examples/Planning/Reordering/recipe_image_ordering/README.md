# Task: recipe_image_ordering

## Task Description:

```
Given a recipe consisting of multiple steps described in natural language and a set of images in randomized order, each depicting one of the steps, your task is to correctly sequence the images to match the order of the corresponding steps in the recipe.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1_3.png)

![Image](1_4.png)

![Image](1_2.png)

![Image](1_1.png)

![Image](1_6.png)

![Image](1_5.png)

```
Example Question: 1.Wash and dry all produce. Adjust rack to upper position and preheat oven to 425 degrees. Bring a large pot of salted water to a boil. Slice zucchini into ¼-inch-thick rounds. Cut tomato into ½-inch-thick wedges. Toss zucchini and tomato with 1 TBSP olive oil and half the Italian seasoning on a baking sheet. Season with salt and pepper.
2.Roast zucchini and tomato in oven until just shy of tender, about 10 minutes. Once water is boiling, add half the orzo from package to pot (use the rest as you like). Cook, stirring occasionally, until al dente, 9-11 minutes. Drain, then return to pot.
3.With your hand on top of one chicken breast, cut ¾ of the way through middle, parallel to cutting board, stopping before you slice through completely. Repeat with other chicken breast. Open each up and season all over with salt, pepper, and remaining Italian seasoning.
4.Heat a drizzle of olive oil in a large pan over medium-high heat. Add chicken and cook until no longer pink in center, 3-4 minutes per side. Remove from pan and set aside on a plate. Meanwhile, cut mozzarella into ½-inch cubes. Halve lemon. Roughly chop parsley.
5.Once veggies have roasted 10 minutes, remove baking sheet from oven. Heat broiler to high or increase oven temperature to 500 degrees. Sprinkle veggies with panko, mozzarella, and Parmesan. Broil (or bake) until panko is golden brown, cheese is melted, and veggies are tender, 3-5 minutes.
6.Add juice from one lemon half and half the parsley to pot with orzo and toss to combine. Season to taste with salt and pepper. Divide orzo between plates. Top with veggies and chicken. Drizzle with any chicken juices from plate and a squeeze of lemon. Garnish with remaining parsley and serve.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 4,3,1,2,6,5
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 3263
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Reordering
- **App**: Planning
- **Input Format**: Photographs
- **Output Format**: multiple_choice
- **Metric Info**:
  - **Field Score Function**: {'order': 'sequence_equality'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'order': 1}}
  - **Response Parse Function**: answer_string
