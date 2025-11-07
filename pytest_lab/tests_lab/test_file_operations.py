
import os
import pytest
from pytest_lab.src_lab.file_utils import (
    create_file,
    read_file,
    append_to_file,
    delete_file,
    write_binary_file,
    read_binary_file,
)

@pytest.mark.files
def test_file_creation_and_deletion(tmp_path):
    """Verify file creation and deletion logic."""
    file_path = tmp_path / "sample.txt"

    create_file(file_path, "Hello Pytest!")
    assert file_path.exists()

    delete_file(file_path)
    assert not file_path.exists()


@pytest.mark.files
def test_read_write_permissions(tmp_path):
    """Ensure files can be read and written."""
    file_path = tmp_path / "data.txt"
    content = "Testing read and write operations"

    create_file(file_path, content)
    assert os.access(file_path, os.R_OK)  # Readable
    assert os.access(file_path, os.W_OK)  # Writable

    read_data = read_file(file_path)
    assert read_data == content


@pytest.mark.files
def test_file_content_validation(tmp_path):
    """Validate file contents after append operations."""
    file_path = tmp_path / "notes.txt"

    create_file(file_path, "Line1\n")
    append_to_file(file_path, "Line2\n")
    content = read_file(file_path)

    assert "Line1" in content
    assert "Line2" in content
    assert content.startswith("Line1")
    assert content.endswith("Line2\n")


@pytest.mark.files
def test_binary_file_operations(tmp_path):
    """Test binary file read/write operations."""
    file_path = tmp_path / "binary_data.bin"
    binary_data = b"\x00\x01\x02\x03\x04"

    write_binary_file(file_path, binary_data)
    assert file_path.exists()

    read_data = read_binary_file(file_path)
    assert read_data == binary_data
    assert isinstance(read_data, bytes)
