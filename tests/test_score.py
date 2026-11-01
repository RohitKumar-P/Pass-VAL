from score_calculator import score

def test_strong_password():
    assert score("Hello123@") == 5

def test_missing_uppercase():
    assert score("hello123@") == 4

def test_missing_special():
    assert score("Hello123") == 4

def test_short_password():
    assert score("Hi@12") == 4