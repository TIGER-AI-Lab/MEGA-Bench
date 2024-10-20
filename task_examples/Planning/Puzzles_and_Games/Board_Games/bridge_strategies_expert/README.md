# Task: bridge_strategies_expert

## Task Description:

```
Given an image of a bridge hand and the bidding process, the task is to generate an optimal declarer strategy, taking into account all possible scenarios. The strategy should be based on analyzing the hand’s distribution, the bidding information, and the potential play of the opponents, aiming to maximize the chances of fulfilling the contract.
Assume West leads first.
	•	Spades: S
	•	Hearts: H
	•	Diamonds: D
	•	Clubs: C
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](01.png)

```
Example Question: West leads the CK against 6S.
What's your strategy?
Example Response: Answer: The only possible danger is a 4-1 heart break. South can guard against this possibility by playing for an elimination.

After winning the opening club lead, South should draw trump ending in the dummy. North's remaining club is ruffed in the closed hand. South now plays 3 rounds of diamonds ruffing the third round. Both clubs and diamonds have been eliminated and a trump remains in both the North and South hands.

South leads a low heart and when West follows low, a low heart is also played from North. East will win, but he will be endplayed. A heart return will allow South to pick up the suit and a minor suit return will concede a ruff and discard.

If West produces a heart honour on the first round of the suit, dummy plays low as before. lf West began with only 1 heart, East can either duck, endplaying his partner, or overtake, endplaying himself.

If West started with 4 hearts to the  HQ, HJ, and H10, East will follow low leaving West endplayed. The contract is guaranteed by playing this way.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 821
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games;Board_Games
- **App**: Planning
- **Input Format**: User Interface Screenshots
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'response': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'response': 1}}
  - **Response Parse Function**: answer_string
