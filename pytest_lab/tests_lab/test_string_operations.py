# tests_lab/test_string_operations.py
import pytest
import requests

@pytest.mark.webtest
def test_string_operations_on_example_dot_com():
    """Test string operations on example.com"""
    # Fetch the webpage
    response = requests.get("https://example.com", verify=False)

    #  1. Ensure request was successful
    assert response.status_code == 200, "Expected status code 200"

    # Get the page text
    page_text = response.text

    #  2. Extract and verify page title
    assert "<title>Example Domain</title>" in page_text, "Page title missing or incorrect"

    #  3. Check if specific text exists on the page
    assert (
        "This domain is for use in illustrative examples in documents." in page_text
        or "This domain is for use in documentation examples without needing permission."
        in page_text
    ), "Expected description text not found"

    # 4. Verify string length constraints
    assert 100 < len(page_text) < 10000, f"Unexpected page length: {len(page_text)}"

    #  5. Test case sensitivity
    assert "example domain" not in page_text, "Lowercase text should not match"
    assert "Example Domain" in page_text, "Proper case text should match"
