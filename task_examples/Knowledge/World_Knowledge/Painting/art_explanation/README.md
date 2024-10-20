# Task: art_explanation

## Task Description:

```
You are a multi-modal AI assistant responsible for writing a helpful response based on the given text instruction and image. Answer in the same language as the question.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](0.png)

```
Example Question: Explain what is amazing about this masterpiece as if you are explaining to a 5-year-old kid. Yet, do not try to skip any details just because the listener is young!
Example Response: Answer: Imagine you have a big box of crayons and you decide to draw the night sky. But instead of just dark sky and tiny, tiny stars, you make the whole sky dance and swirl with lots of blues and greens, and the stars look like big, glowing fireflies. And you don't just color inside the lines; you make the colors go all over the place, with thick, twisty lines that move like waves in the ocean.

This picture is like that! It's made by someone who saw the night in his own special way. He used paint to make the sky look like it's moving, and the stars are so bright and sparkly that they light up everything. It's like he could feel the wind and see the sounds, and he put that feeling on the canvas so that we could feel it too. Isn't it cool that with colors and imagination, you can make a picture that feels alive and full of magic?
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 217
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;World_Knowledge;Painting
- **App**: Knowledge
- **Input Format**: Artistic and Creative Content
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
