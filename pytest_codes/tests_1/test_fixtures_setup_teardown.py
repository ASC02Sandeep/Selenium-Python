import pytest

import tempfile

import os


@pytest.fixture
def temporary_file():
    """Fixture with setup and teardown"""

    # Setup - create temporary file

    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w')

    temp_file.write("Hello, World!\nTest Line 1\nTest Line 2")

    temp_file.close()

    # Provide the file path to tests

    yield temp_file.name

    # Teardown - clean up the file

    if os.path.exists(temp_file.name):
        os.unlink(temp_file.name)


@pytest.fixture
def database_connection():
    """Simulate database connection lifecycle"""

    print("\nSetting up database connection...")

    connection = {"connected": True, "data": []}

    yield connection

    print("Closing database connection...")

    connection["connected"] = False


def test_file_operations(temporary_file):
    """Test reading from temporary file"""

    with open(temporary_file, 'r') as f:
        content = f.read()

    assert "Hello, World!" in content

    assert "Test Line 1" in content

    assert "Test Line 2" in content


def test_database_operations(database_connection):
    """Test database operations"""

    assert database_connection["connected"] == True

    # Simulate adding data

    database_connection["data"].append("test_item")

    assert len(database_connection["data"]) == 1