# Task: planning_screenshot_barman

## Task Description:

```
You are a robot barman that manipulates drink dispensers, shot glasses and a shaker. You have two hands. The goal is to find a plan that serves a desired set of drinks. Here are the 12 actions you can do:

grasp: Grasp a container, format: (grasp [hand] [container])
You can only grasp a container if your hand is empty and it is on the table.
Once you grasp a container, you are holding the container and the container is not on the table.

leave: Leave a container on the table, format: (leave [hand] [container])
You can only leave a container if you are holding it.
Once you leave a container on the table, your hand becomes empty.

fill-shot: Fill a shot glass with an ingredient, format: (fill-shot [shot] [ingredient] [hand-hold] [hand-empty] [dispenser])
You can only fill a shot glass if you are holding the shot glass, your other hand is empty, the shot glass is empty and clean.
Once you fill a shot glass, the shot glass contains the ingredient.

refill-shot: Refill a shot glass with an ingredient, format: (refill-shot [shot] [ingredient] [hand-hold] [hand-empty] [dispenser])
You can only refill a shot glass if you are holding the shot glass, your other hand is empty, the shot glass is empty and has contained the same ingredient before.
Once you refill a shot glass, the shot glass contains the ingredient.

empty-shot: Empty a shot glass, format: (empty-shot [hand] [shot] [beverage])
You can only empty a shot glass if you are holding the shot glass and it contains a beverage.
Once you empty a shot, the shot is empty but not clean.

clean-shot: Clean a shot glass, format: (clean-shot [shot] [beverage] [hand-hold] [hand-empty])
You can only clean a shot glass if you are holding the shot glass and it is empty, and your other hand is empty.
Once you clean a shot, the shot is clean.

pour-shot-to-clean-shaker: Pour an ingredient from a shot glass to a clean shaker, format: (pour-shot-to-clean-shaker [shot] [ingredient] [shaker] [hand] [level-before] [level-after])
You can only pour from a shot glass to a clean shaker if you are holding the shot glass, the shot glass contains an ingredient, and the shaker is empty and clean.
Once you pour an ingredient from a shot glass to a clean shaker, the shaker contains the ingredient and is at one level above the previous level, and the shot glass becomes empty but not clean.

pour-shot-to-used-shaker: Pour an ingredient from a shot glass to a used shaker, format: (pour-shot-to-used-shaker [shot] [ingredient] [shaker] [hand] [level-before] [level-after])
You can only pour from a shot glass to a used shaker if you are holding the shot glass, the shot glass contains an ingredient, the shaker is unshaked and at a level not full.
Once you pour an ingredient from a shot glass to a used shaker, the shaker contains the ingredient and is at one level above the previous level, and the shot glass becomes empty but not clean.

empty-shaker: Empty a shaker, format: (empty-shaker [hand] [shaker] [cocktail] [level-before] [level-empty])
You can only empty a shaker if you are holding the shaker and the shaker contains a shaked cocktail.
Once you empty a shaker, the shaker is at the empty level but not clean.

clean-shaker: Clean a shaker, format: (clean-shaker [hand-hold] [hand-empty] [shaker])
You can only clean a shaker if you are holding the shaker, your other hand is empty, and the shaker is empty.
Once you clean a shaker, the shaker is clean.

shake: Shake a cocktail in a shaker, format: (shake [cocktail] [ingredient-first] [ingredient-second] [shaker] [hand-hold] [hand-empty])
You can only shake a cocktail if you are holding the shaker, your other hand is empty, the shaker is unshaked, and the shaker contains two ingredients, and both ingredients are parts of a cocktail.
Once you shake, the two ingredients in the shaker become a cocktail.

pour-shaker-to-shot: Pour from a shaker to a shot glass, format: (pour-shaker-to-shot [beverage] [shot] [hand] [shaker] [level-before] [level-after])
You can only pour from a shaker to a shot glass if you are holding the shaker, the shaker contains the cocktail, the shaker is shaked, and the shot glass is empty and clean.
Once you pour from a shaker to a shot glass, the shot glass contains the beverage in the shaker, the shot glass is no longer clean and empty, and the shaker is at one level below the previous level.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](barman_p03.png)

```
Example Question: Given a planning problem described as in the image, please provide an executable plan, in the way of a sequence of actions, to solve the problem. Follow the provided action format.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: (grasp left shot4)
(fill-shot shot4 ingredient1 left right dispenser1)
(pour-shot-to-clean-shaker shot4 ingredient1 shaker1 left l0 l1)
(clean-shot shot4 ingredient1 left right)
(fill-shot shot4 ingredient2 left right dispenser2)
(pour-shot-to-used-shaker shot4 ingredient2 shaker1 left l1 l2)
(refill-shot shot4 ingredient2 left right dispenser2)
(leave left shot4)
(grasp right shaker1)
(shake cocktail3 ingredient2 ingredient1 shaker1 right left)
(pour-shaker-to-shot cocktail3 shot3 right shaker1 l2 l1)
(empty-shaker right shaker1 cocktail3 l1 l0)
(clean-shaker right left shaker1)
(leave right shaker1)
(grasp left shot4)
(pour-shot-to-clean-shaker shot4 ingredient2 shaker1 left l0 l1)
(clean-shot shot4 ingredient2 left right)
(fill-shot shot4 ingredient3 left right dispenser3)
(pour-shot-to-used-shaker shot4 ingredient3 shaker1 left l1 l2)
(refill-shot shot4 ingredient3 left right dispenser3)
(leave left shot4)
(grasp right shaker1)
(shake cocktail2 ingredient2 ingredient3 shaker1 right left)
(pour-shaker-to-shot cocktail2 shot1 right shaker1 l2 l1)
(empty-shaker right shaker1 cocktail2 l1 l0)
(clean-shaker right left shaker1)
(leave right shaker1)
(grasp right shot4)
(pour-shot-to-clean-shaker shot4 ingredient3 shaker1 right l0 l1)
(clean-shot shot4 ingredient3 right left)
(fill-shot shot4 ingredient1 right left dispenser1)
(grasp left shaker1)
(pour-shot-to-used-shaker shot4 ingredient1 shaker1 right l1 l2)
(leave right shot4)
(shake cocktail1 ingredient1 ingredient3 shaker1 left right)
(pour-shaker-to-shot cocktail1 shot2 left shaker1 l2 l1)
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 2360
- **Eval Context**: {'task_pddl': '(define (problem prob)\n (:domain barman)\n (:objects \n      shaker1 - shaker\n      left right - hand\n      shot1 shot2 shot3 shot4 - shot\n      ingredient1 ingredient2 ingredient3 - ingredient\n      cocktail1 cocktail2 cocktail3 - cocktail\n      dispenser1 dispenser2 dispenser3 - dispenser\n      l0 l1 l2 - level\n)\n (:init \n  (ontable shaker1)\n  (ontable shot1)\n  (ontable shot2)\n  (ontable shot3)\n  (ontable shot4)\n  (dispenses dispenser1 ingredient1)\n  (dispenses dispenser2 ingredient2)\n  (dispenses dispenser3 ingredient3)\n  (clean shaker1)\n  (clean shot1)\n  (clean shot2)\n  (clean shot3)\n  (clean shot4)\n  (empty shaker1)\n  (empty shot1)\n  (empty shot2)\n  (empty shot3)\n  (empty shot4)\n  (handempty left)\n  (handempty right)\n  (shaker-empty-level shaker1 l0)\n  (shaker-level shaker1 l0)\n  (next l0 l1)\n  (next l1 l2)\n  (cocktail-part1 cocktail1 ingredient1)\n  (cocktail-part2 cocktail1 ingredient3)\n  (cocktail-part1 cocktail2 ingredient2)\n  (cocktail-part2 cocktail2 ingredient3)\n  (cocktail-part1 cocktail3 ingredient1)\n  (cocktail-part2 cocktail3 ingredient2)\n)\n (:goal\n  (and\n      (contains shot1 cocktail1)\n      (contains shot2 cocktail3)\n      (contains shot3 cocktail2)\n)))', 'gt_plan': '(grasp left shot4)\n(fill-shot shot4 ingredient2 left right dispenser2)\n(pour-shot-to-clean-shaker shot4 ingredient2 shaker1 left l0 l1)\n(clean-shot shot4 ingredient2 left right)\n(fill-shot shot4 ingredient1 left right dispenser1)\n(pour-shot-to-used-shaker shot4 ingredient1 shaker1 left l1 l2)\n(refill-shot shot4 ingredient1 left right dispenser1)\n(leave left shot4)\n(grasp right shaker1)\n(shake cocktail3 ingredient1 ingredient2 shaker1 right left)\n(pour-shaker-to-shot cocktail3 shot2 right shaker1 l2 l1)\n(empty-shaker right shaker1 cocktail3 l1 l0)\n(clean-shaker right left shaker1)\n(leave right shaker1)\n(grasp left shot4)\n(pour-shot-to-clean-shaker shot4 ingredient1 shaker1 left l0 l1)\n(clean-shot shot4 ingredient1 left right)\n(fill-shot shot4 ingredient3 left right dispenser3)\n(pour-shot-to-used-shaker shot4 ingredient3 shaker1 left l1 l2)\n(refill-shot shot4 ingredient3 left right dispenser3)\n(leave left shot4)\n(grasp right shaker1)\n(shake cocktail1 ingredient1 ingredient3 shaker1 right left)\n(pour-shaker-to-shot cocktail1 shot1 right shaker1 l2 l1)\n(empty-shaker right shaker1 cocktail1 l1 l0)\n(clean-shaker right left shaker1)\n(leave right shaker1)\n(grasp right shot4)\n(pour-shot-to-clean-shaker shot4 ingredient3 shaker1 right l0 l1)\n(clean-shot shot4 ingredient3 right left)\n(fill-shot shot4 ingredient2 right left dispenser2)\n(grasp left shaker1)\n(pour-shot-to-used-shaker shot4 ingredient2 shaker1 right l1 l2)\n(leave right shot4)\n(shake cocktail2 ingredient2 ingredient3 shaker1 left right)\n(pour-shaker-to-shot cocktail2 shot3 left shaker1 l2 l1)', 'domain_pddl': '(define (domain barman)\n  (:requirements :strips :typing)\n  (:types hand level beverage dispenser container - object\n  \t  ingredient cocktail - beverage\n          shot shaker - container)\n  (:predicates  (ontable ?c - container)\n                (holding ?h - hand ?c - container)\n\t\t(handempty ?h - hand)\n\t\t(empty ?c - container)\n                (contains ?c - container ?b - beverage)\n\t\t(clean ?c - container)\n                (used ?c - container ?b - beverage)\n                (dispenses ?d - dispenser ?i - ingredient)\n\t\t(shaker-empty-level ?s - shaker ?l - level)\n\t\t(shaker-level ?s - shaker ?l - level)\n\t\t(next ?l1 ?l2 - level)\n\t\t(unshaked ?s - shaker)\n\t\t(shaked ?s - shaker)\n                (cocktail-part1 ?c - cocktail ?i - ingredient)\n                (cocktail-part2 ?c - cocktail ?i - ingredient))\n\t\t\n  (:action grasp\n             :parameters (?h - hand ?c - container)\n             :precondition (and (ontable ?c) (handempty ?h))\n             :effect (and (not (ontable ?c))\n\t     \t     \t  (not (handempty ?h))\n\t\t\t  (holding ?h ?c)))\n\n  (:action leave\n             :parameters (?h - hand ?c - container)\n             :precondition (holding ?h ?c)\n             :effect (and (not (holding ?h ?c))\n\t     \t     \t  (handempty ?h)\n\t\t\t  (ontable ?c)))\n  \n  (:action fill-shot\n           :parameters (?s - shot ?i - ingredient ?h1 ?h2 - hand ?d - dispenser)\n           :precondition (and (holding ?h1 ?s)\n                              (handempty ?h2)\n\t   \t\t      (dispenses ?d ?i)\n                              (empty ?s)\n\t\t\t      (clean ?s))\n           :effect (and (not (empty ?s))\n\t   \t   \t(contains ?s ?i)\n\t   \t   \t(not (clean ?s))\n\t\t\t(used ?s ?i)))\n\n\n  (:action refill-shot\n           :parameters (?s - shot ?i - ingredient ?h1 ?h2 - hand ?d - dispenser)\n           :precondition (and (holding ?h1 ?s)\t   \t\t      \n                              (handempty ?h2)\n\t   \t\t      (dispenses ?d ?i)\n                              (empty ?s)\n\t\t\t      (used ?s ?i))\n           :effect (and (not (empty ?s))\n                        (contains ?s ?i)))\n\n  (:action empty-shot\n           :parameters (?h - hand ?p - shot ?b - beverage)\n           :precondition (and (holding ?h ?p)\n                              (contains ?p ?b))\n           :effect (and (not (contains ?p ?b))\n\t   \t   \t(empty ?p)))\n\n  (:action clean-shot\n  \t   :parameters (?s - shot ?b - beverage ?h1 ?h2 - hand)\n           :precondition (and (holding ?h1 ?s)\n                              (handempty ?h2)\t   \t\t      \n\t\t\t      (empty ?s)\n                              (used ?s ?b))\n           :effect (and (not (used ?s ?b))\n\t   \t   \t(clean ?s)))\n\n  (:action pour-shot-to-clean-shaker\n           :parameters (?s - shot ?i - ingredient ?d - shaker ?h1 - hand ?l ?l1 - level)\n           :precondition (and (holding ?h1 ?s)\n\t\t\t      (contains ?s ?i)\n                              (empty ?d)\n\t   \t\t      (clean ?d)                              \n                              (shaker-level ?d ?l)\n                              (next ?l ?l1))\n           :effect (and (not (contains ?s ?i))\n\t   \t   \t(empty ?s)\n\t\t\t(contains ?d ?i)\n                        (not (empty ?d))\n\t\t\t(not (clean ?d))\n\t\t\t(unshaked ?d)\n\t\t\t(not (shaker-level ?d ?l))\n\t\t\t(shaker-level ?d ?l1)))\n\n\n  (:action pour-shot-to-used-shaker\n           :parameters (?s - shot ?i - ingredient ?d - shaker ?h1 - hand ?l ?l1 - level)\n           :precondition (and (holding ?h1 ?s)\n\t\t\t      (contains ?s ?i)\n                              (unshaked ?d)\n                              (shaker-level ?d ?l)\n                              (next ?l ?l1))\n           :effect (and (not (contains ?s ?i))\n                        (contains ?d ?i)\n\t   \t   \t(empty ?s)     \n  \t\t\t(not (shaker-level ?d ?l))\n\t\t\t(shaker-level ?d ?l1)))\n\n  (:action empty-shaker\n           :parameters (?h - hand ?s - shaker ?b - cocktail ?l ?l1 - level)\n           :precondition (and (holding ?h ?s)\n                              (contains ?s ?b)\n\t\t\t      (shaked ?s)\n\t\t\t      (shaker-level ?s ?l)\n\t\t\t      (shaker-empty-level ?s ?l1))\n           :effect (and (not (shaked ?s))\n\t   \t   \t(not (shaker-level ?s ?l))\n\t   \t   \t(shaker-level ?s ?l1)\n\t\t\t(not (contains ?s ?b))\n\t   \t   \t(empty ?s)))\n\n  (:action clean-shaker\n  \t   :parameters (?h1 ?h2 - hand ?s - shaker)\n           :precondition (and (holding ?h1 ?s)\n                              (handempty ?h2)\n                              (empty ?s))\n           :effect (and (clean ?s)))\n  \n  (:action shake\n  \t   :parameters (?b - cocktail ?d1 ?d2 - ingredient ?s - shaker ?h1 ?h2 - hand)\n           :precondition (and (holding ?h1 ?s)\n                              (handempty ?h2)\n\t\t\t      (contains ?s ?d1)\n                              (contains ?s ?d2)\n                              (cocktail-part1 ?b ?d1)\n\t\t\t      (cocktail-part2 ?b ?d2)\n\t\t\t      (unshaked ?s))\t\t\t      \n           :effect (and (not (unshaked ?s))\n\t\t        (not (contains ?s ?d1))\n                        (not (contains ?s ?d2))\n\t   \t   \t(shaked ?s)\n                        (contains ?s ?b)))\n\n  (:action pour-shaker-to-shot\n           :parameters (?b - beverage ?d - shot ?h - hand ?s - shaker ?l ?l1 - level)\n           :precondition (and (holding ?h ?s)\n\t\t\t      (shaked ?s)\n\t\t\t      (empty ?d)\n\t\t\t      (clean ?d)\n\t\t\t      (contains ?s ?b)\n                              (shaker-level ?s ?l)\n                              (next ?l1 ?l))\n           :effect (and (not (clean ?d))\n\t   \t   \t(not (empty ?d))\n\t\t\t(contains ?d ?b)\n\t\t\t(shaker-level ?s ?l1)\n\t\t\t(not (shaker-level ?s ?l))))\n )'}
- **Taxonomy Tree Path**: Planning;Agents_and_Planning;Symbolic_Planning
- **App**: Planning
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'plan': 'symbolic_planning_test'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'plan': 1}}
  - **Response Parse Function**: answer_string
