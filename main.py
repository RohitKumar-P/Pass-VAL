import getpass
from validator import validate_password
from space_checker import space_checker
from empty_pass_check import empty_check
from suggestions import password_suggestions
from score_calculator import score
from strength_checker import check_strength
from entropy_calculator import calculate_entropy

print("=" * 40)
print("             SECUREPASS")
print("       Password Security Analyzer")
print("=" * 40)

password = getpass.getpass("\nEnter your password: ")

while empty_check(password) or space_checker(password):
    if empty_check(password):
        print("Error: Password cannot be empty!")
    else:
        print("Error: Password cannot contain whitespace!")

    password = getpass.getpass("\nEnter your password: ")

numeric_score = score(password)
strength = check_strength(numeric_score)
entropy = calculate_entropy(password)
valid = validate_password(password)
suggestions = password_suggestions(password)

print("\n------------ ANALYSIS REPORT ------------")

print(f"Password Status   : {'VALID' if valid else 'INVALID'}")
print(f"Security Score    : {numeric_score}/5")
print(f"Strength          : {strength}")
print(f"Estimated Entropy : {entropy} bits")

print("\nSuggestions:")

if not suggestions:
    print("  No improvements required.")
else:
    for suggestion in suggestions:
        print(f"  - {suggestion}")

print("\n-----------------------------------------")
print("          Analysis Complete")
print("-----------------------------------------")