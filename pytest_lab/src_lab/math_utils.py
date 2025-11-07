# src_lab/math_utils.py
import math
from statistics import mean, median

def fibonacci(n: int):
    """Return Fibonacci sequence up to n terms."""
    if n <= 0:
        raise ValueError("n must be positive")
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def calculate_mean(values):
    """Return mean of numbers."""
    if not values:
        raise ValueError("List cannot be empty")
    return mean(values)

def calculate_median(values):
    """Return median of numbers."""
    if not values:
        raise ValueError("List cannot be empty")
    return median(values)

def circle_area(radius: float) -> float:
    """Return area of a circle (πr²)."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius**2

def rectangle_area(length: float, width: float) -> float:
    """Return area of a rectangle."""
    if length < 0 or width < 0:
        raise ValueError("Dimensions cannot be negative")
    return length * width
