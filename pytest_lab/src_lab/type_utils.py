

class Person:
    """Simple custom class for instance type validation."""
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

def greet(name: str) -> str:
    """Return greeting string."""
    return f"Hello, {name}!"

def to_int(value):
    """Convert value to int, raises ValueError for invalid input."""
    return int(value)

def multiply(a, b):
    """Multiply only numeric values, raise TypeError for invalid types."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both parameters must be numbers")
    return a * b
