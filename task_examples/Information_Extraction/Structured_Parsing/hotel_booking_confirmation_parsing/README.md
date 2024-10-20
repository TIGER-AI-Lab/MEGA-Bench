# Task: hotel_booking_confirmation_parsing

## Task Description:

```
Given a screenshot of a hotel booking confirmation page, extract the following specific information:

(1) Hotel Name
(2) Hotel Address
(3) Hotel Rating
(4) Number of Reviews
(5) Check-in Date and Time
(6) Check-out Date and Time
(7) Length of Stay
(8) Total Price
(9) Tax and Fees
(10) Cancellation Fee

If any of the above information is not present in the image, leave it blank.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](hotel_booking_confirmation_parsing1.png)

```
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: {'name': 'Holiday Inn Columbus Dwtn-Capitol Square, an IHG Hotel', 'address': '175 East Town Street, Columbus, OH 43215, United States of America', 'rating': '7.5', 'reviews': '517', 'check_in': 'Sun, Sep 15, 2024, From: 4:00 PM', 'check_out': 'Mon, Sep 16, 2024, Until 12:00 PM', 'length': '1 night', 'total': '$118.67', 'tax': '$17.67', 'cancell': '$118.67'}
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 1927
- **Eval Context**: {}
- **Taxonomy Tree Path**: Information_Extraction;Structured_Parsing
- **App**: Information_Extraction
- **Input Format**: User Interface Screenshots
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'name': 'exact_str_match', 'address': 'exact_str_match', 'rating': 'exact_str_match', 'reviews': 'exact_str_match', 'check_in': 'exact_str_match', 'check_out': 'exact_str_match', 'length': 'exact_str_match', 'total': 'exact_str_match', 'tax': 'exact_str_match', '': 'exact_str_match', 'cancell': 'exact_str_match'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'name': 1, 'address': 1, 'rating': 1, 'reviews': 1, 'check_in': 1, 'check_out': 1, 'length': 1, 'total': 1, 'tax': 1, '': 1, 'cancell': 1}}
  - **Response Parse Function**: json
