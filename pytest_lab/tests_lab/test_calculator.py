import pytest
from pytest_lab.src_lab.calculator import Calculator  # Adjust import path as needed

@pytest.fixture
def cal():
    """Fixture for calculator"""
    return Calculator()

def test_addition_positive_and_negative(cal):
    assert cal.add(10, 5) == 15
    assert cal.add(-3, -7) == -10
    assert cal.add(-5, 10) == 5

def test_division_with_zero(cal):
    assert cal.divide(10, 2) == 5
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        cal.divide(8, 0)

def test_multiplication_with_decimals(cal):
    assert cal.multiply(2.5, 4.0) == pytest.approx(10.0)
    assert cal.multiply(3.3, 0.0) == 0.0
    assert cal.multiply(-1.5, 2.0) == -3.0

def test_power_operations(cal):
    assert cal.power(2, 3) == 8
    assert cal.power(2, -1) == 0.5
    assert cal.power(5, 0) == 1
