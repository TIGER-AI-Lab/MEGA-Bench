# Task: multi_lingual_manual_explanation_scooter_Spanish

## Task Description:

```
Según el contenido de las imágenes del manual de usuario proporcionado, responde las preguntas en español. Para problemas relacionados con el funcionamiento, proporciona soluciones. Para cuestiones de seguridad personal, ofrece recomendaciones razonables.
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
Example Question: ¿Este scooter tiene función de iluminación? Si es así, ¿cómo se enciende?
Example Response: Answer: Sí, el scooter está equipado con iluminación LED y puede encenderla o apagarla siguiendo estos pasos:

​	1.	Asegúrese de que el scooter esté encendido: presione el botón de encendido para encender el scooter.

​	2.	Encender la luz: con el scooter encendido, presione brevemente el botón de encendido una vez para encender la luz LED frontal.

​	3.	Apagar la luz: vuelva a presionar brevemente el botón de encendido para apagar la luz LED.
Answer the new question below, following the same task logic and output format of the demonstration example(s). Do not output additional contents that violate the specified format.
```

## Additional Task Information:

- **ID**: 877
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Detailed_Manual_Understanding
- **App**: Information_Extraction
- **Input Format**: Text-Based Images and Documents
- **Output Format**: open_ended_output
- **Metric Info**:
  - **Field Score Function**: {'reference': 'gpt_4o_as_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'reference': 1}}
  - **Response Parse Function**: answer_string
