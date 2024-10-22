# Task: Bridge strategies worldclass

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
Example Response: Answer: West leads the SQ against 3NT. 
South has 4 tricks (the SA,SK, HA, and CA) outside of diamonds. South should try to take 5diamond tricks. lf diamonds are 3-2 there will be no problem.
Considering the diamond suit in isolation, South has a well known safety play available to guard
against 4 diamonds to the DQ in East's hand. The safety play involves leading a low diamond
from North towards the  DJ.
On this deal, it would be wrong to take this safety play. lf South wins the spade lead in dummy tolead a low diamond towards the DJ, East will play the DQ if he has it. South will have 5 diamondtricks, but the suit will be blocked. The defense will switch to hearts eventually knocking outdummy's side entry, the HA. South will go down if diamonds are 4-1.
South cannot quard against 4 diamonds to the DQ in East's hand. The only 4-1 diamond breaksSouth can guard against are singleton Queen with either West or East. South should win the SA in his hand and immediately duck a diamond.
The defenders can attack only 1 of dummy's entries. South can unblock the diamonds and dummy
will still have an entry to get to the good diamonds.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Information:

- **Sample ID**: 807
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Planning;Puzzles_and_Games;Board_Games
- **Application**: Planning
- **Input Format**: Diagrams and Data Visualizations
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'response': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'response': 1}}
  - **Response Parse Function**: answer_string
- **Source Description**: Data and answer are collected from Bridge Master 2000
