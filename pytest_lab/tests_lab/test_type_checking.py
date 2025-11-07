
import pytest
from pytest_lab.src_lab.type_utils import (
    add_numbers,
    greet,
    to_int,
    multiply,
    Person,
)

@pytest.mark.types
def test_function_return_types():
    """Verify that functions return expected data types."""
    result_add = add_numbers(5, 3)
    result_greet = greet("Alice")

    assert isinstance(result_add, int)
    assert isinstance(result_greet, str)
    assert type(result_greet) is str


@pytest.mark.types
def test_parameter_type_enforcement():
    """Ensure function enforces parameter types properly."""
    # Valid call
    assert multiply(3, 4) == 12

    # Invalid calls should raise TypeError
    with pytest.raises(TypeError, match="Both parameters must be numbers"):
        multiply("a", 5)

    with pytest.raises(TypeError):
        multiply(10, None)


@pytest.mark.types
def test_type_conversion_functions():
    """Test type conversion utilities like to_int."""
    assert to_int("10") == 10
    assert isinstance(to_int("42"), int)

    with pytest.raises(ValueError):
        to_int("invalid_number")


@pytest.mark.types
def test_custom_class_instance_validation():
    """Validate creation and instance type of custom class."""
    p = Person("Bob", 25)

    assert isinstance(p, Person)
    assert isinstance(p.name, str)
    assert isinstance(p.age, int)
    assert type(p.age) is int
