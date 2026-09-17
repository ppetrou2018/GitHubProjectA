
from github_project_a.calculator import add, multiply


def test_add():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_decimal_numbers():
    assert add(1.5, 2.5) == 4.0


def test_multiply():
    assert multiply(2, 3) == 6


def test_multiply_negative_numbers():
    assert multiply(-2, 3) == -6


def test_multiply_by_zero():
    assert multiply(10, 0) == 0
