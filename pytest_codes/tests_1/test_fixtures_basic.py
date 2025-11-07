import pytest


@pytest.fixture
def sample_data():
    """Fixture that returns sample data for tests"""

    return [1, 2, 3, 4, 5]


@pytest.fixture
def calculator():
    """Fixture that provides a Calculator instance"""

    from pytest_codes.src.calculator import Calculator

    return Calculator()


def test_sum_with_fixture(sample_data):
    assert sum(sample_data) == 15


def test_calculator_add(calculator):
    result = calculator.add(5, 3)

    assert result == 8


def test_calculator_multiply(calculator):
    result = calculator.multiply(4, 7)

    assert result == 28