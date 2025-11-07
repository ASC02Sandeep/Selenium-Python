
import pytest

@pytest.mark.data
def test_list_sorting_algorithms():
    """Verify list sorting behavior"""
    data = [5, 3, 8, 1, 2]
    sorted_data = sorted(data)
    assert sorted_data == [1, 2, 3, 5, 8]
    assert sorted_data[0] == min(data)
    assert sorted_data[-1] == max(data)

@pytest.mark.data
def test_dictionary_key_value_pairs():
    """Check dictionary key-value integrity"""
    student = {"name": "Alice", "age": 21, "course": "CS"}
    assert "name" in student
    assert student["age"] == 21
    assert student.get("course") == "CS"
    assert len(student) == 3

@pytest.mark.data
def test_set_operations_union_intersection():
    """Test set operations: union and intersection"""
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    union_result = set_a | set_b
    intersection_result = set_a & set_b
    assert union_result == {1, 2, 3, 4, 5}
    assert intersection_result == {3}
    assert len(union_result) == 5
    assert len(intersection_result) == 1

@pytest.mark.data
def test_list_comprehensions_with_assertions():
    """Validate list comprehension logic"""
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    assert squares == [1, 4, 9, 16, 25]
    assert all(s > 0 for s in squares)
    assert len(squares) == len(numbers)
