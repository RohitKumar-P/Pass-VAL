def check_strength(score):
    
    if score<=2:
        return "Weak"
    elif score<=4:
        return "Moderate"
    else:
        return "Strong"