
import os

def create_file(file_path: str, content: str = ""):
    """Create a text file with given content."""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return file_path

def read_file(file_path: str) -> str:
    """Read text content from a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def append_to_file(file_path: str, text: str):
    """Append text to an existing file."""
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(text)

def delete_file(file_path: str):
    """Delete file if it exists."""
    if os.path.exists(file_path):
        os.remove(file_path)

def write_binary_file(file_path: str, data: bytes):
    """Write binary data to a file."""
    with open(file_path, "wb") as f:
        f.write(data)

def read_binary_file(file_path: str) -> bytes:
    """Read binary data from a file."""
    with open(file_path, "rb") as f:
        return f.read()
