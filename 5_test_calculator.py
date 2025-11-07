import pytest

# ---------------- FIXTURES ---------------- #

@pytest.fixture(scope="function")
def function_scope_fixture():
    """Runs for each test function"""
    print("\nFunction fixture setup")
    yield "function_data"
    print("Function fixture teardown")


@pytest.fixture(scope="class")
def class_scope_fixture():
    """Runs once per test class"""
    print("\nClass fixture setup")
    yield "class_data"
    print("Class fixture teardown")


@pytest.fixture(scope="module")
def module_scope_fixture():
    """Runs once per test module"""
    print("\nModule fixture setup")
    yield "module_data"
    print("Module fixture teardown")


# ---------------- CALCULATOR CLASSES ---------------- #

class BasicCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


class AdvancedCalculator:
    def multiply(self, a, b):
        return a * b

    def power(self, a, b):
        return a ** b


# ---------------- TEST CLASSES ---------------- #

@pytest.mark.usefixtures("class_scope_fixture", "module_scope_fixture")
class TestBasicCalculator:

    def test_add(self, function_scope_fixture):
        calc = BasicCalculator()
        assert calc.add(10, 5) == 15

    def test_subtract(self, function_scope_fixture):
        calc = BasicCalculator()
        assert calc.subtract(10, 5) == 5


@pytest.mark.usefixtures("class_scope_fixture", "module_scope_fixture")
class TestAdvancedCalculator:

    def test_multiply(self, function_scope_fixture):
        calc = AdvancedCalculator()
        assert calc.multiply(3, 4) == 12

    def test_power(self, function_scope_fixture):
        calc = AdvancedCalculator()
        assert calc.power(2, 3) == 8
