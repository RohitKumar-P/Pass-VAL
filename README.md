# Pass VAL

A Python-based password strength analyzer that evaluates password complexity, estimates theoretical entropy, validates password requirements, and provides improvement suggestions.

## Features

- Password strength scoring (0–5)
- Strength classification: Weak, Moderate, Strong
- Entropy estimation in bits
- Validation of password requirements
- Detection of whitespace and empty passwords
- Suggestions for improving password strength
- Hidden password input using Python's `getpass`
- Automated unit testing with pytest

## Project Structure

```text
SecurePass/
├── main.py
├── validator.py
├── score_calculator.py
├── strength_checker.py
├── entropy_calculator.py
├── space_checker.py
├── empty_pass_check.py
├── suggestions.py
├── requirements.txt
└── tests/
