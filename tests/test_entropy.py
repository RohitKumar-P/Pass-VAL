from entropy_calculator import calculate_entropy

def test_entropy():
    result = calculate_entropy("Hello123@")
    assert result > 0

def test_empty_password():
    result = calculate_entropy("")
    assert result == 0

def test_known_entropy():
    assert calculate_entropy("Hello123@") == 54.98

def test_lowercase_only():
    assert calculate_entropy("abcdefgh") == 37.6