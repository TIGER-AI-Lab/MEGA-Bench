# Task: Weather info parsing

## Task Description:

```
Given a screenshot of a weather webpage, extract the following information:
(1) Current Temperature (°C)
(2) Cloud cover (%)
(3) High/Low Temperature for today (°C)
(4) Wind Speed (km/h)
(5) Wind Gust (km/h)
(6) Wind Direction (°)
(7) Humidity (%)
(8) Dew Point (°C)
(9) UV Index
(10) Air Quality Index (AQI)
(11) Visibility (km)
(12) Pressure (mb)
(13) Sunrise time
(14) Sunset time
(15) Moonrise time
(16) Moonset time
(17) Phase of moon (%)
(18) Next time full moon
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](weather_info_parsing1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'current_temp': '24', 'cloud': '85', 'high_low_temp': '24, 22', 'wind_speed': '18', 'wind_gust': '29', 'wind_direction': 'E, 79', 'humidity': '85', 'dew_point': '21', 'UV': '6', 'AQI': '35', 'visibility': '15', 'pressure': '1012', 'sunrise': '6:15', 'sunset': '8:30', 'moonrise': '10:19', 'moonset': '10:21', 'phase_moon': '25', 'next_full_moon': 'Aug 19'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Information:

- **Sample ID**: 269
- **Eval Context (for this query sample)**: {}
- **Taxonomy Tree Path**: Information_Extraction;Structured_Parsing
- **Application**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'current_temp': 'simple_str_match', 'cloud': 'simple_str_match', 'high_low_temp': 'simple_str_match', 'wind_speed': 'simple_str_match', 'wind_gust': 'simple_str_match', 'wind_direction': 'simple_str_match', 'humidity': 'simple_str_match', 'dew_point': 'simple_str_match', 'UV': 'simple_str_match', 'AQI': 'simple_str_match', 'visibility': 'simple_str_match', 'pressure': 'simple_str_match', 'sunrise': 'simple_str_match', 'sunset': 'simple_str_match', 'moonrise': 'simple_str_match', 'moonset': 'simple_str_match', 'phase_moon': 'simple_str_match', 'next_full_moon': 'simple_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'current_temp': 1, 'cloud': 1, 'high_low_temp': 1, 'wind_speed': 1, 'wind_gust': 1, 'wind_direction': 1, 'humidity': 1, 'dew_point': 1, 'UV': 1, 'AQI': 1, 'visibility': 1, 'pressure': 1, 'sunrise': 1, 'sunset': 1, 'moonrise': 1, 'moonset': 1, 'phase_moon': 1, 'next_full_moon': 1}}
  - **Response Parse Function**: json
- **Source Description**: Images were collected from the Microsoft Weather by taking screenshots. Questions and answers were designed by the annotator.
