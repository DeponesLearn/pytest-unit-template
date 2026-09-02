from src.calculator import summination, substraction, multiplication, division

def test_summation():

    assert summination(2, 10) == 12
    assert summination(3, 5) == 8
    assert summination(4, 6) == 10

def test_subtraction():

    assert substraction(8, 2) == 6
    assert substraction(7, 5) == 2
    assert substraction(4, 2) == 2

def test_multiplication():

    assert multiplication(2, 2) == 4
    assert multiplication(7, 2) == 14
    assert multiplication(10, 2) == 20

def test_Division():
    """
    Testing Division function
    """
    assert division(5, 5) == 1
    assert division(70, 10) == 7
    assert division(16, 4) == 4
