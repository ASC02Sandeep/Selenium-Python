import pytest

from pytest_codes.src.calculator import Calculator


@pytest.mark.parametrize("a,b,expected_exception", [

    (10, 0, ValueError),

    (5, 0, ValueError),

    (-10, 0, ValueError)

])
def test_division_by_zero_parameterized(a, b, expected_exception):
    calc = Calculator()

    with pytest.raises(expected_exception):
        calc.divide(a, b)


@pytest.mark.parametrize("negative_number", [-1, -5, -10, -100])
def test_factorial_negative_parameterized(negative_number):
    calc = Calculator()

    with pytest.raises(ValueError, match="Factorial not defined for negative numbers"):
        calc.factorial(negative_number)