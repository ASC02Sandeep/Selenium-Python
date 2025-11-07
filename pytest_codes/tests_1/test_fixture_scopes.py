import pytest


@pytest.fixture(scope="function")
def function_scope_fixture():
    """Runs for each test function (default)"""

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


@pytest.fixture(scope="session")
def session_scope_fixture():
    """Runs once per test session"""

    print("\nSession fixture setup")

    yield "session_data"

    print("Session fixture teardown")


class TestFixtureScopes:

    def test_one(self, function_scope_fixture, class_scope_fixture,

                 module_scope_fixture, session_scope_fixture):
        assert function_scope_fixture == "function_data"

    def test_two(self, function_scope_fixture, class_scope_fixture,

                 module_scope_fixture, session_scope_fixture):
        assert class_scope_fixture == "class_data"