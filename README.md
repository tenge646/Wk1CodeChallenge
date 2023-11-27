# Wk1CodeChallenge

## Code Challenge Solutions

This repository contains Python scripts solving three different coding challenges. Each challenge is implemented in a separate file.

## Challenges

### Challenge 1: Time Conversion
File: `time_conversion.py`

This script provides a function `time_conversion()` that converts a 12-hour time format to a 24-hour time format. It takes hour, minute, and period ("am" or "pm") as input and returns a four-digit string encoding the time in 24-hour format.

### Challenge 2: Two Numbers are Positive
File: `two_positive.py`

The `two_positive()` function in this script checks if exactly two out of three integers are positive numbers. It takes three integers (a, b, c) as arguments and returns `True` if exactly two of them are positive, otherwise `False`.

### Challenge 3: Consonant Value
File: `consonant_value.py`

The `solve()` function in this script finds the highest value of consonant substrings in a given lowercase string containing only alphabetic characters. It calculates the value of consonants based on their positions in the alphabet and returns the highest value of consonant substrings.

## Usage

To use these scripts, you can directly call the functions with appropriate arguments.

Example:

## Example usage of time_conversion.py
```from challenge1.time_conversion import time_conversion

result = time_conversion(8, 30, "am")
print("Time in 24-hour format:", result)

```
## How to Run
Execute the Python scripts by running them directly using Python:
`python3 time_conversion.py`        
`python3 two_positive.py`        
`python3 consonant_value.py`       


## Author  
Tenge

## License
This project is licensed under the MIT License.