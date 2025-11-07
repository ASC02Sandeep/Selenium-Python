
import pytest
from math import pi, isclose
from pytest_lab.src_lab.math_utils import (
    fibonacci,
    is_prime,
    calculate_mean,
    calculate_median,
    circle_area,
    rectangle_area,
)

@pytest.mark.math
def test_fibonacci_sequence_generation():
    """Verify Fibonacci sequence generation with edge cases."""
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(8)[-1] == 13  # last term check

    with pytest.raises(ValueError, match="n must be positive"):
        fibonacci(0)

@pytest.mark.math
def test_prime_number_identification():
    """Check correctness of prime number identification."""
    primes = [2, 3, 5, 7, 11, 13, 17]
    non_primes = [0, 1, 4, 6, 8, 9, 10]

    for p in primes:
        assert is_prime(p) is True

    for n in non_primes:
        assert is_prime(n) is False

@pytest.mark.math
def test_statistical_calculations():
    """Validate mean and median calculations."""
    data = [2, 4, 6, 8, 10]

    assert calculate_mean(data) == pytest.approx(6)
    assert calculate_median(data) == 6

    # Edge case: odd-length list
    assert calculate_median([1, 3, 5]) == 3

    # Empty list should raise
    with pytest.raises(ValueError):
        calculate_mean([])
    with pytest.raises(ValueError):
        calculate_median([])

@pytest.mark.math
def test_geometric_formula_validations():
    """Test geometric area calculations."""
    assert isclose(circle_area(1), pi, rel_tol=1e-6)
    assert isclose(circle_area(2), pi * 4, rel_tol=1e-6)
    assert rectangle_area(5, 10) == 50

    # Negative dimensions → ValueError
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        circle_area(-1)

    with pytest.raises(ValueError):
        rectangle_area(5, -3)
