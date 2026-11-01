def space_checker(password):
    for character in password:
        if character.isspace():
            return True

    return False