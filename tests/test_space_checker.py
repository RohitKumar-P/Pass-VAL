from space_checker import space_checker

def test_normal_space():
    assert space_checker("Hello World") == True

def test_tab():
    assert space_checker("Hello\tWorld") == True

def test_newline():
    assert space_checker("Hello\nWorld") == True

def test_no_space():
    assert space_checker("Hello123@") == False