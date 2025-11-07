
import pytest
from pytest_lab.src_lab.custom_exceptions import InvalidOperationError

@pytest.mark.exceptions
def test_division_by_zero_error():
    """Verify division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0

@pytest.mark.exceptions
def test_file_not_found_exception(tmp_path):
    """Check handling of missing files."""
    missing_file = tmp_path / "non_existent.txt"
    with pytest.raises(FileNotFoundError):
        with open(missing_file, "r") as f:
            f.read()

@pytest.mark.exceptions
def test_invalid_type_conversion():
    """Ensure invalid type conversion raises ValueError."""
    with pytest.raises(ValueError, match="invalid literal"):
        int("not_a_number")

@pytest.mark.exceptions
def test_custom_exception_with_message():
    """Test custom exception behavior and message."""
    with pytest.raises(InvalidOperationError, match="Operation not allowed"):
        raise InvalidOperationError("Operation not allowed")
