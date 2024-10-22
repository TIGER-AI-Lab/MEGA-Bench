# Task: Planning screenshot termes

## Task Description:

```
You control a robot that can take the following actions to build complex structures.

move: Move from a position to another, format: (move [pos_from] [pos_to] [height])
The new position and the old position must be at the same height.

move-up: Move up from a position to another, format: (move-up [pos_from] [height_from] [pos_to] [height_to])
The height at the new position is one block higher than the old position.

move-down: Move down from a position to another, format: (move-down [pos_from] [height_from] [pos_to] [height_to])
The height at the new position is one block lower than the old position.

place-block: Place a block at a neighboring position from the robot's current position, format: (place-block [pos_at] [pos_place] [height_at] [height_place])
The robot must have a block. The current height at the robot's position and the block's position must be the same. A block cannot be placed at the depot. The height at the block's position will be one block higher than the current height.

remove-block: Remove a block at a neighboring position from the robot's current position, format: (remove-block [pos_at] [pos_remove] [height_at] [height_remove])
The robot must not have a block. A block cannot be removed from the depot. The current height at the robot's position must be the same as the new height at the block's position. The new height at the block's position will be one block lower than the current height.

create-block: Create a block at the depot, format: (create-block [pos])
The robot will have the block.

destroy-block: Destroy a block at the depot, format: (destroy-block [pos])
The robot must have a block.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](termes_3.png)

```
Example Question: Given a planning problem described as in the image, please provide an executable plan, in the way of a sequence of actions, to solve the problem. Follow the provided action format.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: (create-block pos-2-0)
(move pos-2-0 pos-3-0 n0)
(place-block pos-3-0 pos-3-1 n0 n1)
(move pos-3-0 pos-2-0 n0)
(create-block pos-2-0)
(place-block pos-2-0 pos-3-0 n0 n1)
(create-block pos-2-0)
(move-up pos-2-0 n0 pos-3-0 n1)
(place-block pos-3-0 pos-3-1 n1 n2)
(move-down pos-3-0 n1 pos-2-0 n0)
(remove-block pos-2-0 pos-3-0 n1 n0)
(move pos-2-0 pos-2-1 n0)
(move pos-2-1 pos-2-2 n0)
(place-block pos-2-2 pos-2-1 n0 n1)
(move-up pos-2-2 n0 pos-2-1 n1)
(remove-block pos-2-1 pos-3-1 n2 n1)
(move pos-2-1 pos-3-1 n1)
(place-block pos-3-1 pos-2-1 n1 n2)
(move-down pos-3-1 n1 pos-3-0 n0)
(move pos-3-0 pos-2-0 n0)
(create-block pos-2-0)
(place-block pos-2-0 pos-3-0 n0 n1)
(create-block pos-2-0)
(move-up pos-2-0 n0 pos-3-0 n1)
(place-block pos-3-0 pos-3-1 n1 n2)
(move-down pos-3-0 n1 pos-2-0 n0)
(create-block pos-2-0)
(move-up pos-2-0 n0 pos-3-0 n1)
(move-up pos-3-0 n1 pos-3-1 n2)
(place-block pos-3-1 pos-2-1 n2 n3)
(move-down pos-3-1 n2 pos-3-0 n1)
(move-down pos-3-0 n1 pos-2-0 n0)
(remove-block pos-2-0 pos-3-0 n1 n0)
(move pos-2-0 pos-1-0 n0)
(move pos-1-0 pos-1-1 n0)
(move pos-1-1 pos-1-2 n0)
(move pos-1-2 pos-2-2 n0)
(place-block pos-2-2 pos-3-2 n0 n1)
(move-up pos-2-2 n0 pos-3-2 n1)
(move-up pos-3-2 n1 pos-3-1 n2)
(remove-block pos-3-1 pos-2-1 n3 n2)
(move-down pos-3-1 n2 pos-3-2 n1)
(move-down pos-3-2 n1 pos-2-2 n0)
(move pos-2-2 pos-1-2 n0)
(place-block pos-1-2 pos-1-1 n0 n1)
(move pos-1-2 pos-2-2 n0)
(remove-block pos-2-2 pos-3-2 n1 n0)
(move pos-2-2 pos-3-2 n0)
(place-block pos-3-2 pos-2-2 n0 n1)
(move-up pos-3-2 n0 pos-2-2 n1)
(move-down pos-2-2 n1 pos-1-2 n0)
(remove-block pos-1-2 pos-1-1 n1 n0)
(move-up pos-1-2 n0 pos-2-2 n1)
(move-up pos-2-2 n1 pos-2-1 n2)
(place-block pos-2-1 pos-3-1 n2 n3)
(move-down pos-2-1 n2 pos-2-2 n1)
(move-down pos-2-2 n1 pos-3-2 n0)
(remove-block pos-3-2 pos-2-2 n1 n0)
(move pos-3-2 pos-2-2 n0)
(move pos-2-2 pos-1-2 n0)
(move pos-1-2 pos-0-2 n0)
(move pos-0-2 pos-0-1 n0)
(place-block pos-0-1 pos-1-1 n0 n1)
(move-up pos-0-1 n0 pos-1-1 n1)
(remove-block pos-1-1 pos-2-1 n2 n1)
(move pos-1-1 pos-2-1 n1)
(move-down pos-2-1 n1 pos-2-0 n0)
(destroy-block pos-2-0)
(remove-block pos-2-0 pos-2-1 n1 n0)
(move pos-2-0 pos-2-1 n0)
(move-up pos-2-1 n0 pos-1-1 n1)
(move-down pos-1-1 n1 pos-0-1 n0)
(place-block pos-0-1 pos-0-2 n0 n1)
(move-up pos-0-1 n0 pos-1-1 n1)
(move-down pos-1-1 n1 pos-2-1 n0)
(remove-block pos-2-1 pos-1-1 n1 n0)
(move pos-2-1 pos-1-1 n0)
(place-block pos-1-1 pos-2-1 n0 n1)
(move-up pos-1-1 n0 pos-2-1 n1)
(move-down pos-2-1 n1 pos-2-2 n0)
(remove-block pos-2-2 pos-2-1 n1 n0)
(place-block pos-2-2 pos-3-2 n0 n1)
(move pos-2-2 pos-1-2 n0)
(remove-block pos-1-2 pos-0-2 n1 n0)
(place-block pos-1-2 pos-2-2 n0 n1)
(move-up pos-1-2 n0 pos-2-2 n1)
(move-down pos-2-2 n1 pos-2-1 n0)
(remove-block pos-2-1 pos-2-2 n1 n0)
(place-block pos-2-1 pos-1-1 n0 n1)
(move pos-2-1 pos-2-0 n0)
(create-block pos-2-0)
(move pos-2-0 pos-2-1 n0)
(place-block pos-2-1 pos-2-2 n0 n1)
(remove-block pos-2-1 pos-1-1 n1 n0)
(move-up pos-2-1 n0 pos-2-2 n1)
(place-block pos-2-2 pos-3-2 n1 n2)
(move-down pos-2-2 n1 pos-2-1 n0)
(remove-block pos-2-1 pos-2-2 n1 n0)
(move pos-2-1 pos-2-0 n0)
(place-block pos-2-0 pos-2-1 n0 n1)
(create-block pos-2-0)
(move-up pos-2-0 n0 pos-2-1 n1)
(move-down pos-2-1 n1 pos-2-2 n0)
(place-block pos-2-2 pos-1-2 n0 n1)
(remove-block pos-2-2 pos-2-1 n1 n0)
(move pos-2-2 pos-2-1 n0)
(place-block pos-2-1 pos-2-2 n0 n1)
(move-up pos-2-1 n0 pos-2-2 n1)
(move pos-2-2 pos-1-2 n1)
(move-down pos-1-2 n1 pos-1-1 n0)
(remove-block pos-1-1 pos-1-2 n1 n0)
(move pos-1-1 pos-2-1 n0)
(move pos-2-1 pos-2-0 n0)
(place-block pos-2-0 pos-2-1 n0 n1)
(create-block pos-2-0)
(move-up pos-2-0 n0 pos-2-1 n1)
(place-block pos-2-1 pos-2-2 n1 n2)
(move-down pos-2-1 n1 pos-2-0 n0)
(create-block pos-2-0)
(move-up pos-2-0 n0 pos-2-1 n1)
(move-up pos-2-1 n1 pos-2-2 n2)
(place-block pos-2-2 pos-3-2 n2 n3)
(move-down pos-2-2 n2 pos-2-1 n1)
(move-down pos-2-1 n1 pos-2-0 n0)
(create-block pos-2-0)
(move-up pos-2-0 n0 pos-2-1 n1)
(move-up pos-2-1 n1 pos-2-2 n2)
(move-up pos-2-2 n2 pos-3-2 n3)
(place-block pos-3-2 pos-3-1 n3 n4)
(move-down pos-3-2 n3 pos-2-2 n2)
(remove-block pos-2-2 pos-3-2 n3 n2)
(move-down pos-2-2 n2 pos-2-1 n1)
(move-down pos-2-1 n1 pos-2-0 n0)
(destroy-block pos-2-0)
(move-up pos-2-0 n0 pos-2-1 n1)
(remove-block pos-2-1 pos-2-2 n2 n1)
(move pos-2-1 pos-2-2 n1)
(move-down pos-2-2 n1 pos-1-2 n0)
(move pos-1-2 pos-1-1 n0)
(place-block pos-1-1 pos-1-0 n0 n1)
(move-up pos-1-1 n0 pos-2-1 n1)
(move-down pos-2-1 n1 pos-2-0 n0)
(remove-block pos-2-0 pos-1-0 n1 n0)
(destroy-block pos-2-0)
(remove-block pos-2-0 pos-2-1 n1 n0)
(destroy-block pos-2-0)
(move pos-2-0 pos-2-1 n0)
(move-up pos-2-1 n0 pos-2-2 n1)
(remove-block pos-2-2 pos-3-2 n2 n1)
(move-down pos-2-2 n1 pos-1-2 n0)
(place-block pos-1-2 pos-1-1 n0 n1)
(remove-block pos-1-2 pos-2-2 n1 n0)
(move pos-1-2 pos-2-2 n0)
(place-block pos-2-2 pos-2-1 n0 n1)
(move pos-2-2 pos-1-2 n0)
(remove-block pos-1-2 pos-1-1 n1 n0)
(move pos-1-2 pos-1-1 n0)
(place-block pos-1-1 pos-1-0 n0 n1)
(move-up pos-1-1 n0 pos-2-1 n1)
(move-down pos-2-1 n1 pos-2-0 n0)
(remove-block pos-2-0 pos-2-1 n1 n0)
(destroy-block pos-2-0)
(move pos-2-0 pos-2-1 n0)
(move pos-2-1 pos-2-2 n0)
(remove-block pos-2-2 pos-3-2 n1 n0)
(place-block pos-2-2 pos-2-1 n0 n1)
(move-up pos-2-2 n0 pos-2-1 n1)
(move-down pos-2-1 n1 pos-2-0 n0)
(remove-block pos-2-0 pos-1-0 n1 n0)
(destroy-block pos-2-0)
(remove-block pos-2-0 pos-2-1 n1 n0)
(destroy-block pos-2-0)
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 4662
- **Eval Context (for this query sample)**: {'task_pddl': '(define (problem termes-00038-0036-4x3x3-random_towers_4x3_3_1_3)\n(:domain termes)\n; termes-00038-0036-4x3x3-random_towers_4x3_3_1_3\n; Initial state:\n;  0   0  R0D  0\n;  0   0   0   0\n;  0   0   0   0\n; Goal state:\n;  0   0   0   0\n;  0   0   0   0\n;  0   3   0   0\n; Maximal height: 3\n(:objects\n    n0 - numb\n    n1 - numb\n    n2 - numb\n    n3 - numb\n    pos-0-0 - position\n    pos-0-1 - position\n    pos-0-2 - position\n    pos-1-0 - position\n    pos-1-1 - position\n    pos-1-2 - position\n    pos-2-0 - position\n    pos-2-1 - position\n    pos-2-2 - position\n    pos-3-0 - position\n    pos-3-1 - position\n    pos-3-2 - position\n)\n(:init\n    (height pos-0-0 n0)\n    (height pos-0-1 n0)\n    (height pos-0-2 n0)\n    (height pos-1-0 n0)\n    (height pos-1-1 n0)\n    (height pos-1-2 n0)\n    (height pos-2-0 n0)\n    (height pos-2-1 n0)\n    (height pos-2-2 n0)\n    (height pos-3-0 n0)\n    (height pos-3-1 n0)\n    (height pos-3-2 n0)\n    (at pos-2-0)\n    (SUCC n1 n0)\n    (SUCC n2 n1)\n    (SUCC n3 n2)\n    (NEIGHBOR pos-0-0 pos-1-0)\n    (NEIGHBOR pos-0-0 pos-0-1)\n    (NEIGHBOR pos-0-1 pos-1-1)\n    (NEIGHBOR pos-0-1 pos-0-0)\n    (NEIGHBOR pos-0-1 pos-0-2)\n    (NEIGHBOR pos-0-2 pos-1-2)\n    (NEIGHBOR pos-0-2 pos-0-1)\n    (NEIGHBOR pos-1-0 pos-0-0)\n    (NEIGHBOR pos-1-0 pos-2-0)\n    (NEIGHBOR pos-1-0 pos-1-1)\n    (NEIGHBOR pos-1-1 pos-0-1)\n    (NEIGHBOR pos-1-1 pos-2-1)\n    (NEIGHBOR pos-1-1 pos-1-0)\n    (NEIGHBOR pos-1-1 pos-1-2)\n    (NEIGHBOR pos-1-2 pos-0-2)\n    (NEIGHBOR pos-1-2 pos-2-2)\n    (NEIGHBOR pos-1-2 pos-1-1)\n    (NEIGHBOR pos-2-0 pos-1-0)\n    (NEIGHBOR pos-2-0 pos-3-0)\n    (NEIGHBOR pos-2-0 pos-2-1)\n    (NEIGHBOR pos-2-1 pos-1-1)\n    (NEIGHBOR pos-2-1 pos-3-1)\n    (NEIGHBOR pos-2-1 pos-2-0)\n    (NEIGHBOR pos-2-1 pos-2-2)\n    (NEIGHBOR pos-2-2 pos-1-2)\n    (NEIGHBOR pos-2-2 pos-3-2)\n    (NEIGHBOR pos-2-2 pos-2-1)\n    (NEIGHBOR pos-3-0 pos-2-0)\n    (NEIGHBOR pos-3-0 pos-3-1)\n    (NEIGHBOR pos-3-1 pos-2-1)\n    (NEIGHBOR pos-3-1 pos-3-0)\n    (NEIGHBOR pos-3-1 pos-3-2)\n    (NEIGHBOR pos-3-2 pos-2-2)\n    (NEIGHBOR pos-3-2 pos-3-1)\n    (IS-DEPOT pos-2-0)\n)\n(:goal\n(and\n    (height pos-0-0 n0)\n    (height pos-0-1 n0)\n    (height pos-0-2 n0)\n    (height pos-1-0 n0)\n    (height pos-1-1 n0)\n    (height pos-1-2 n3)\n    (height pos-2-0 n0)\n    (height pos-2-1 n0)\n    (height pos-2-2 n0)\n    (height pos-3-0 n0)\n    (height pos-3-1 n0)\n    (height pos-3-2 n0)\n    (not (has-block))\n)\n)\n)', 'gt_plan': '(create-block pos-2-0)\n(move pos-2-0 pos-1-0 n0)\n(place-block pos-1-0 pos-1-1 n0 n1)\n(move pos-1-0 pos-2-0 n0)\n(create-block pos-2-0)\n(move pos-2-0 pos-1-0 n0)\n(move-up pos-1-0 n0 pos-1-1 n1)\n(move-down pos-1-1 n1 pos-1-2 n0)\n(move pos-1-2 pos-2-2 n0)\n(place-block pos-2-2 pos-1-2 n0 n1)\n(move pos-2-2 pos-2-1 n0)\n(remove-block pos-2-1 pos-1-1 n1 n0)\n(move pos-2-1 pos-2-2 n0)\n(place-block pos-2-2 pos-2-1 n0 n1)\n(move-up pos-2-2 n0 pos-1-2 n1)\n(move-down pos-1-2 n1 pos-1-1 n0)\n(move pos-1-1 pos-1-0 n0)\n(move pos-1-0 pos-2-0 n0)\n(create-block pos-2-0)\n(move pos-2-0 pos-1-0 n0)\n(place-block pos-1-0 pos-1-1 n0 n1)\n(move-up pos-1-0 n0 pos-1-1 n1)\n(move pos-1-1 pos-2-1 n1)\n(move-down pos-2-1 n1 pos-3-1 n0)\n(remove-block pos-3-1 pos-2-1 n1 n0)\n(move pos-3-1 pos-2-1 n0)\n(move-up pos-2-1 n0 pos-1-1 n1)\n(place-block pos-1-1 pos-1-2 n1 n2)\n(move-down pos-1-1 n1 pos-2-1 n0)\n(remove-block pos-2-1 pos-1-1 n1 n0)\n(move pos-2-1 pos-2-2 n0)\n(place-block pos-2-2 pos-2-1 n0 n1)\n(move-up pos-2-2 n0 pos-2-1 n1)\n(move-down pos-2-1 n1 pos-1-1 n0)\n(remove-block pos-1-1 pos-2-1 n1 n0)\n(move pos-1-1 pos-0-1 n0)\n(place-block pos-0-1 pos-0-0 n0 n1)\n(move pos-0-1 pos-1-1 n0)\n(move pos-1-1 pos-1-0 n0)\n(remove-block pos-1-0 pos-0-0 n1 n0)\n(place-block pos-1-0 pos-1-1 n0 n1)\n(move pos-1-0 pos-2-0 n0)\n(create-block pos-2-0)\n(place-block pos-2-0 pos-2-1 n0 n1)\n(create-block pos-2-0)\n(move-up pos-2-0 n0 pos-2-1 n1)\n(place-block pos-2-1 pos-1-1 n1 n2)\n(move-down pos-2-1 n1 pos-2-0 n0)\n(create-block pos-2-0)\n(move-up pos-2-0 n0 pos-2-1 n1)\n(move-up pos-2-1 n1 pos-1-1 n2)\n(place-block pos-1-1 pos-1-2 n2 n3)\n(move-down pos-1-1 n2 pos-2-1 n1)\n(move-down pos-2-1 n1 pos-2-0 n0)\n(remove-block pos-2-0 pos-2-1 n1 n0)\n(place-block pos-2-0 pos-1-0 n0 n1)\n(move-up pos-2-0 n0 pos-1-0 n1)\n(remove-block pos-1-0 pos-1-1 n2 n1)\n(move-down pos-1-0 n1 pos-2-0 n0)\n(destroy-block pos-2-0)\n(move pos-2-0 pos-2-1 n0)\n(remove-block pos-2-1 pos-1-1 n1 n0)\n(move pos-2-1 pos-2-0 n0)\n(destroy-block pos-2-0)\n(remove-block pos-2-0 pos-1-0 n1 n0)\n(destroy-block pos-2-0)', 'domain_pddl': '(define (domain termes)\n(:requirements :typing :negative-preconditions)\n(:types\n    numb - object\n    position - object\n)\n(:predicates\n    (height ?p - position ?h - numb)\n    (at ?p - position)\n    (has-block)\n    ;\n    ; static predicates\n    (SUCC ?n1 - numb ?n2 - numb)\n    (NEIGHBOR ?p1 - position ?p2 - position)\n    (IS-DEPOT ?p - position)\n)\n(:action move\n    :parameters (?from - position ?to - position ?h - numb)\n    :precondition\n    (and\n        (at ?from)\n        (NEIGHBOR ?from ?to)\n        (height ?from ?h)\n        (height ?to ?h)\n    )\n    :effect\n    (and\n        (not (at ?from))\n        (at ?to)\n    )\n)\n\n(:action move-up\n    :parameters (?from - position ?hfrom - numb ?to - position ?hto - numb)\n    :precondition\n    (and\n        (at ?from)\n        (NEIGHBOR ?from ?to)\n        (height ?from ?hfrom)\n        (height ?to ?hto)\n        (SUCC ?hto ?hfrom)\n    )\n    :effect\n    (and\n        (not (at ?from))\n        (at ?to)\n    )\n)\n\n(:action move-down\n    :parameters (?from - position ?hfrom - numb ?to - position ?hto - numb)\n    :precondition\n    (and\n        (at ?from)\n        (NEIGHBOR ?from ?to)\n        (height ?from ?hfrom)\n        (height ?to ?hto)\n        (SUCC ?hfrom ?hto)\n    )\n    :effect\n    (and\n        (not (at ?from))\n        (at ?to)\n    )\n)\n\n(:action place-block\n    :parameters (?rpos - position ?bpos - position ?hbefore - numb ?hafter - numb)\n    :precondition\n    (and\n        (at ?rpos)\n        (NEIGHBOR ?rpos ?bpos)\n        (height ?rpos ?hbefore)\n        (height ?bpos ?hbefore)\n        (SUCC ?hafter ?hbefore)\n        (has-block)\n        (not (IS-DEPOT ?bpos))\n    )\n    :effect\n    (and\n        (not (height ?bpos ?hbefore))\n        (height ?bpos ?hafter)\n        (not (has-block))\n    )\n)\n\n(:action remove-block\n    :parameters (?rpos - position ?bpos - position ?hbefore - numb ?hafter - numb)\n    :precondition\n    (and\n        (at ?rpos)\n        (NEIGHBOR ?rpos ?bpos)\n        (height ?rpos ?hafter)\n        (height ?bpos ?hbefore)\n        (SUCC ?hbefore ?hafter)\n        (not (has-block))\n    )\n    :effect\n    (and\n        (not (height ?bpos ?hbefore))\n        (height ?bpos ?hafter)\n        (has-block)\n    )\n)\n\n(:action create-block\n    :parameters (?p - position)\n    :precondition\n    (and\n        (at ?p)\n        (not (has-block))\n        (IS-DEPOT ?p)\n    )\n    :effect\n    (and\n        (has-block)\n    )\n)\n\n(:action destroy-block\n    :parameters (?p - position)\n    :precondition\n    (and\n        (at ?p)\n        (has-block)\n        (IS-DEPOT ?p)\n    )\n    :effect\n    (and\n        (not (has-block))\n    )\n)\n\n)'}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning;Symbolic_Planning
- **Application**: Planning
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'plan': 'symbolic_planning_test'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'plan': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from website, and the questions and answers are adapted to match the transitions from init state to goal state
