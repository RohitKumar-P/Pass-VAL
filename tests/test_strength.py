from strength_checker import check_strength

def test_weak():
    assert check_strength(2) == "Weak"

def test_moderate():
    assert check_strength(3) == "Moderate"

def test_strong():
    assert check_strength(5) == "Strong"