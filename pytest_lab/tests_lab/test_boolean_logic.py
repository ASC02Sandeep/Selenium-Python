
import pytest

@pytest.mark.boolean
def test_multiple_and_or_conditions():
    """Test complex AND/OR boolean conditions"""
    age = 25
    country = "India"
    is_student = True

    # Complex condition
    result = (age > 18 and country == "India") or is_student
    assert result is True

    # Negative scenario
    result = (age < 18 and country == "India") or not is_student
    assert result is False


@pytest.mark.boolean
def test_truthy_and_falsy_evaluations():
    """Verify truthy and falsy values"""
    assert bool(1) is True
    assert bool("Hello") is True
    assert bool([1, 2, 3]) is True

    # Falsy values
    assert bool(0) is False
    assert bool("") is False
    assert bool([]) is False
    assert bool(None) is False


@pytest.mark.boolean
def test_none_type_checking():
    """Check None type and equality"""
    value = None
    assert value is None
    assert not value  # None is falsy
    assert value is not True
    assert value is not False


@pytest.mark.boolean
def test_empty_collections_validation():
    """Validate empty and non-empty collections"""
    empty_list = []
    empty_dict = {}
    empty_set = set()
    non_empty_list = [1, 2, 3]

    # Empty collections are falsy
    assert not empty_list
    assert not empty_dict
    assert not empty_set

    # Non-empty collections are truthy
    assert non_empty_list
    assert bool(non_empty_list) is True
    assert len(empty_list) == 0
    assert len(non_empty_list) > 0
