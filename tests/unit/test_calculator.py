from src.calculator import add, sub, mul, div

def test_summation():

    assert add(2, 10) == 12
    assert add(3, 5) == 8
    assert add(4, 6) == 10

def test_subtraction():

    assert sub(8, 2) == 6
    assert sub(7, 5) == 2
    assert sub(4, 2) == 2

def test_multiplication():

    assert mul(2, 2) == 4
    assert mul(7, 2) == 14
    assert mul(10, 2) == 20

def test_Division():
    """
    Testing Division function
    """
    assert div(5, 5) == 1
    assert div(70, 10) == 7
    assert div(16, 4) == 4
