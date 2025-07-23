import pytest

from src.calculator import addition, subtraction, multiplication, division


def test_addition( ):
    res = addition(20, 10)
    assert res == 30

def test_subtraction( ):
    res = subtraction(10, 5)
    assert res == 5

def test_multiplication( ):
    res = multiplication(20, 5)
    assert res == 100

def test_division_posdate( ):
    res = division(10, 5)
    assert res == 2

def test_division_exception( ):
    with pytest.raises(ZeroDivisionError):
        division(10, 0)