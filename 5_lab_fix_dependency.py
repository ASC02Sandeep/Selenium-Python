import pytest

@pytest.fixture
def employee_basic():
    """Base employee data"""
    return {"name": "John Doe", "id": 101}


@pytest.fixture
def employee_role(employee_basic):
    """Fixture depending on employee_basic"""
    role_info = employee_basic.copy()
    role_info["role"] = "Software Engineer"
    role_info["department"] = "IT"
    return role_info


@pytest.fixture
def employee_full(employee_role):
    """Final fixture depending on previous two"""
    employee_role["salary"] = 85000
    employee_role["employment_type"] = "Full-Time"
    return employee_role


def test_employee_role(employee_role):
    assert employee_role["name"] == "John Doe"
    assert employee_role["role"] == "Software Engineer"
    assert employee_role["department"] == "IT"


def test_employee_full(employee_full):
    assert employee_full["id"] == 101
    assert employee_full["salary"] == 85000
    assert employee_full["employment_type"] == "Full-Time"
