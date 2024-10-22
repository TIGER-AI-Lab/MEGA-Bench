# Task: Planning screenshot blocksworld

## Task Description:

```
The domain assumes a world where there are a set of blocks that can be stacked on top of each other, an arm that can hold one block at a time, and a table where blocks can be placed. The robot has 4 actions:

pickup: allows the arm to pick up a block from the table if it is clear and the arm is empty, format: (pickup [object])
After the pickup action, the arm will be holding the block, and the block will no longer be on the table or clear.

putdown: allows the arm to put down a block on the table if it is holding a block, format: (putdown [object])
After the putdown action, the arm will be empty, and the block will be on the table and clear.

stack: allows the arm to stack a block on top of another block if the arm is holding the top block and the bottom block is clear, format: (stack [object] [object-under])
After the stack action, the arm will be empty, the top block will be on top of the bottom block, and the bottom block will no longer be clear.

unstack: allows the arm to unstack a block from on top of another block if the arm is empty and the top block is clear, format: (unstack [object] [object-under])
After the unstack action, the arm will be holding the top block, the top block will no longer be on top of the bottom block, and the bottom block will be clear.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](blocksworld_p3.png)

```
Example Question: Given a planning problem described as in the image, please provide an executable plan, in the way of a sequence of actions, to solve the problem. Follow the provided action format.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: (unstack b1 b3)
(putdown b1)
(unstack b3 b2)
(stack b3 b4)
(pickup b2)
(stack b2 b1)
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3777
- **Eval Context (for this query sample)**: {'task_pddl': '(define (problem BW-rand-3)\n(:domain blocksworld-4ops)\n(:objects b1 b2 b3 )\n(:init\n(arm-empty)\n(on-table b1)\n(on b2 b3)\n(on b3 b1)\n(clear b2)\n)\n(:goal\n(and\n(on b2 b3)\n(on b3 b1))\n)\n)', 'gt_plan': '', 'domain_pddl': '(define (domain blocksworld-4ops)\n  (:requirements :strips)\n(:predicates (clear ?x)\n             (on-table ?x)\n             (arm-empty)\n             (holding ?x)\n             (on ?x ?y))\n\n(:action pickup\n  :parameters (?ob)\n  :precondition (and (clear ?ob) (on-table ?ob) (arm-empty))\n  :effect (and (holding ?ob) (not (clear ?ob)) (not (on-table ?ob)) \n               (not (arm-empty))))\n\n(:action putdown\n  :parameters  (?ob)\n  :precondition (holding ?ob)\n  :effect (and (clear ?ob) (arm-empty) (on-table ?ob) \n               (not (holding ?ob))))\n\n(:action stack\n  :parameters  (?ob ?underob)\n  :precondition (and (clear ?underob) (holding ?ob))\n  :effect (and (arm-empty) (clear ?ob) (on ?ob ?underob)\n               (not (clear ?underob)) (not (holding ?ob))))\n\n(:action unstack\n  :parameters  (?ob ?underob)\n  :precondition (and (on ?ob ?underob) (clear ?ob) (arm-empty))\n  :effect (and (holding ?ob) (clear ?underob)\n               (not (on ?ob ?underob)) (not (clear ?ob)) (not (arm-empty)))))'}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning;Symbolic_Planning
- **Application**: Planning
- **Input Format**: Text-Based Images and Documents
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'plan': 'symbolic_planning_test'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'plan': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from website, and the questions and answers are adapted to match the transitions from init state to goal state
