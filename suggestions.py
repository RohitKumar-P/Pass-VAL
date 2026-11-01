
def password_suggestions(password):

    suggestions = []

    upper = False
    lower = False
    digit = False
    special = False

    for i in password:

        if i.isupper():
            upper = True

        elif i.islower():
            lower = True

        elif i.isdigit():
            digit = True

        else:
            special = True

    if not upper:
        suggestions.append("Add an uppercase letter.")

    if not lower:
        suggestions.append("Add a lowercase letter.")

    if not digit:
        suggestions.append("Add a number.")

    if not special:
        suggestions.append("Add a special character.")

    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")

    return suggestions
