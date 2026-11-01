import math

def calculate_entropy(password):
    L = len(password)

    pool = 0

    lower = False
    Upper = False
    digit = False
    special = False


    special_chars = "@#$^!?~"

    for i in password:
        if i.islower():
            lower = True
        elif i.isupper():
            Upper = True
        elif i.isdigit():
            digit = True
        elif i in special_chars:
            special = True
    if lower:
        pool +=26
    if Upper:
        pool +=26
    if digit:
        pool +=10
    if special:
        pool +=7
    if pool == 0:
        return 0

    entropy_ = L*math.log2(pool)

    return round(entropy_, 2)