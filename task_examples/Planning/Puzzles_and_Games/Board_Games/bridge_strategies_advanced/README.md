# Task: bridge_strategies_advanced

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
Example Response: Answer: West leads the HK against 6S
South wins the trick with the HA.South's H2 can go away on North's CK leaving South's only possible losers in the diamond suit.

If diamonds prove to be 3-3 or 4-2, South can easily take all 13 tricks. He could cash the CA, cross to the DK, discard the H2 on the CK, cash the DA, and cross-ruff the rest of the tricks high.

As South needs only 12 tricks, he should try to quard against a 5-1 diamond break. The above line of play will fail againet this distribution if West ruffs South's DA and returns a trump.

South should start as described, but the second round of diamonds should be ducked!
East must return a trump to stop a cross-ruff. South can now ruff a low diamond, ruff back to hishand, and ruff the last low diamond. South ruffs back to his hand again. lf trumps prove to be 3-2South can draw the defenders' remaining trumps and cash the  A at trick 13.

The distribution of the defensive spades is only relevant when the diamonds divide 5-1. Had West followed to the second diamond, South would not need to ruff as many clubs in his hand.

Notice, however, South will go down if he draws even 1 round of trump at the start of the play.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 793
- **Eval Context**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games;Board_Games
- **App**: Planning
- **Input Format**: User Interface Screenshots
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'response': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'response': 1}}
  - **Response Parse Function**: answer_string
