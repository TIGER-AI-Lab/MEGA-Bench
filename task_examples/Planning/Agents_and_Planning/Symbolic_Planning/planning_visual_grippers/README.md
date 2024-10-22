# Task: Planning visual grippers

## Task Description:

```
You have a set of robots, each with a gripper that can move objects between different rooms. There are 3 actions defined in this domain:

move: this action allows a robot to move from one room to another, format: (move [robot] [room_from] [room_to])
The action has a single precondition, which is that the robot is currently in a room.
The effect of this action is to move the robot to another room and to remove the fact that it is in the original room.

pick: this action allows a robot to pick up an object using the gripper, format: (pick [robot] [object] [room] [gripper])
The action has three preconditions: (1) the object is located in a room (2) the robot is currently in the same room and (3) the gripper is free (i.e., not holding any object).
The effect of this action is to update the state of the world to show that the robot is carrying the object using the gripper, the object is no longer in the room, and the gripper is no longer free.

drop: this action allows a robot to drop an object that it is carrying, format: (drop [robot] [object] [room] [gripper])
The action has two preconditions: (1) the robot is currently carrying the object using the gripper, and (2) the robot is currently in a room.
The effect of this action is to update the state of the world to show that the robot is no longer carrying the object using the gripper, the object is now located in the room, and the gripper is now free.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](init_state_3.png)

![Image](goal_state_3.png)

```
Example Question: You are provided with two images. The first describes the initial state and the second describes the goal state. Robots can be in any room at the goal state.
Please output an executable plan to reach the goal state, in the way of a sequence of actions, to solve the problem. Follow the provided action format.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: (pick robot1 ball1 room1 lgripper1)
(pick robot1 ball2 room1 rgripper1)
(move robot1 room1 room4)
(drop robot1 ball2 room4 rgripper1)
(move robot1 room4 room5)
(drop robot1 ball1 room5 lgripper1)
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 3792
- **Eval Context (for this query sample)**: {'task_pddl': '(define (problem gripper-2-2-2)\n(:domain gripper-strips)\n(:objects robot1 robot2 - robot\nrgripper1 lgripper1 rgripper2 lgripper2 - gripper\nroom1 room2 - room\nball1 ball2 - object)\n(:init\n(at-robby robot1 room1)\n(free robot1 rgripper1)\n(free robot1 lgripper1)\n(at-robby robot2 room1)\n(free robot2 rgripper2)\n(free robot2 lgripper2)\n(at ball1 room1)\n(at ball2 room1)\n)\n(:goal\n(and\n(at ball1 room1)\n(at ball2 room1)\n)\n)\n)', 'gt_plan': '', 'domain_pddl': '(define (domain gripper-strips)\n (:requirements :strips :typing) \n (:types room object robot gripper)\n (:predicates (at-robby ?r - robot ?x - room)\n \t      (at ?o - object ?x - room)\n\t      (free ?r - robot ?g - gripper)\n\t      (carry ?r - robot ?o - object ?g - gripper))\n\n   (:action move\n       :parameters  (?r - robot ?from ?to - room)\n       :precondition (and  (at-robby ?r ?from))\n       :effect (and  (at-robby ?r ?to)\n\t\t     (not (at-robby ?r ?from))))\n\n   (:action pick\n       :parameters (?r - robot ?obj - object ?room - room ?g - gripper)\n       :precondition  (and  (at ?obj ?room) (at-robby ?r ?room) (free ?r ?g))\n       :effect (and (carry ?r ?obj ?g)\n\t\t    (not (at ?obj ?room)) \n\t\t    (not (free ?r ?g))))\n\n   (:action drop\n       :parameters (?r - robot ?obj - object ?room - room ?g - gripper)\n       :precondition  (and  (carry ?r ?obj ?g) (at-robby ?r ?room))\n       :effect (and (at ?obj ?room)\n\t\t    (free ?r ?g)\n\t\t    (not (carry ?r ?obj ?g)))))'}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning;Symbolic_Planning
- **Application**: Planning
- **Input Format**: Artistic and Creative Content
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'plan': 'symbolic_planning_test'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'plan': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data collected from website, and the questions and answers are adapted to match the transitions from init state to goal state
