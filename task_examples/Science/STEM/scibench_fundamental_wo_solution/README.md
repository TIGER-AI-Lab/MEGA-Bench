# Task: scibench_fundamental_wo_solution

## Task Description:

```
Solve the problem. The answer is a number.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: Figure shows an overhead view of two particles moving at constant momentum along horizontal paths. Particle 1, with momentum magnitude $p_1=5.0 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s}$, has position vector $\vec{r}_1$ and will pass $2.0 \mathrm{~m}$ from point $O$. Particle 2 , with momentum magnitude $p_2=2.0 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s}$, has position vector $\vec{r}_2$ and will pass $4.0 \mathrm{~m}$ from point $O$. What is the magnitude of the net angular momentum $\vec{L}$ about point $O$ of the two-particle system?
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: 2.0
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2873
- **Eval Context**: {}
- **Taxonomy Tree Path**: Science;STEM
- **App**: Science
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: numerical_data
- **Metric Info**:
  - **Field Score Function**: {'Answer': 'general_single_numerical_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Answer': 1}}
  - **Response Parse Function**: answer_string
