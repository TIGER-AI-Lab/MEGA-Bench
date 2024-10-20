# Task: ascii_art_30

## Task Description:

```
Your task is to generate the ASCII art by turning the attached image into tone-based ASCII art with a maximum width of 30 characters. The foreground should be text while the background should be spaces.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](birdie.png)

```
Example Response: Answer:         ----=                 
      ---::----               
    --:::::::---=             
   =---::::::::--=            
  -------::::::-----          
 ==----------:---=----        
-==--------------==-----      
 ===-=------=---==---==%%+--  
=========--==---=----+%#-:::--
+++===========--=====@#-::::--
   =+++++++++=======%@+-------
                     #+=======
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 1
- **Eval Context**: {}
- **Taxonomy Tree Path**: Knowledge;Arts
- **App**: Knowledge
- **Input Format**: Photographs
- **Output Format**: contextual_formatted_text
- **Metric Info**:
  - **Field Score Function**: {'ascii art': 'ascii_art_gpt4o_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'ascii art': 1}}
  - **Response Parse Function**: ascii_answer_string
