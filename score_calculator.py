
def score(password):

    points = 0

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

    if len(password) >= 8:
        points += 1

    if upper:
        points += 1

    if lower:
        points += 1

    if digit:
        points += 1

    if special:
        points += 1

    return points
