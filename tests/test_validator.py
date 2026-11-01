from validator import validate_password

def test_valid_password():
    assert validate_password("Hello123@") == True

def test_missing_uppercase():
    assert validate_password("hello123@") == False

def test_missing_digit():
    assert validate_password("Helloabc@") == False