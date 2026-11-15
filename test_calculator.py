
from calculator import add, subtract


def test_addition():
    assert add(10, 5) == 15


def test_subtraction():
    assert subtract(10, 5) == 5


def test_addition_negative():
    assert add(-5, 3) == -2


def test_subtraction_negative():
    assert subtract(-5, -3) == -2
