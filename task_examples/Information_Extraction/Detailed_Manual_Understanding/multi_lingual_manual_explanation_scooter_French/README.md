# Task: multi_lingual_manual_explanation_scooter_French

## Task Description:

```
Répondez aux questions en français en fonction du contenu de l’image du manuel d’utilisation fourni. Pour les questions liées aux opérations, proposez des solutions. Pour les questions concernant la sécurité personnelle, fournissez des conseils raisonnables.
```

![Image](1.png)

![Image](2.png)

![Image](3.png)

![Image](4.png)

![Image](5.png)

![Image](6.png)

![Image](7.png)

![Image](8.png)

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
Example Question: Est-ce que la trottinette a une fonction d’éclairage ? Si oui, comment l’allumer ?
Example Response: Answer: Oui, la trottinette est équipée d’un éclairage LED. Voici comment l’allumer ou l’éteindre :

​	1.	Assurez-vous que la trottinette est allumée : Appuyez sur le bouton d’alimentation pour mettre la trottinette en marche.

​	2.	Allumer la lumière : Lorsque la trottinette est allumée, appuyez brièvement sur le bouton d’alimentation une fois pour allumer le phare LED avant.

​	3.	Éteindre la lumière : Appuyez de nouveau brièvement sur le bouton d’alimentation pour éteindre la lumière LED.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 863
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Detailed_Manual_Understanding
- **App**: Information_Extraction
- **Input Format**: Text-Based Images and Documents
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
