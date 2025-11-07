
import pytest
from pytest_lab.src_lab.regex_utils import (
    is_valid_email,
    is_valid_phone,
    is_strong_password,
    extract_domain_from_url,
)

@pytest.mark.regex
def test_email_validation_patterns():
    """Test valid and invalid email addresses."""
    valid_emails = ["test@example.com", "user.name@domain.co", "user123@my-site.org"]
    invalid_emails = ["plainaddress", "user@.com", "name@domain", "test@domain.c"]

    for email in valid_emails:
        assert is_valid_email(email)

    for email in invalid_emails:
        assert not is_valid_email(email)


@pytest.mark.regex
def test_phone_number_formats():
    """Test multiple phone number patterns."""
    valid_numbers = ["9876543210", "+91-9876543210", "+1 1234567890"]
    invalid_numbers = ["12345", "abcd567890", "+999999999999999"]

    for num in valid_numbers:
        assert is_valid_phone(num)

    for num in invalid_numbers:
        assert not is_valid_phone(num)


@pytest.mark.regex
def test_password_strength_rules():
    """Verify password strength rules."""
    strong_passwords = ["Abcdef1@", "StrongPass9$", "My@Pass2025"]
    weak_passwords = ["password", "12345678", "NoSpecial1", "short@1A"]

    for pwd in strong_passwords:
        assert is_strong_password(pwd)

    for pwd in weak_passwords:
        assert not is_strong_password(pwd)


@pytest.mark.regex
def test_url_parsing_and_validation():
    """Extract and validate domains from URLs."""
    assert extract_domain_from_url("https://www.google.com") == "google.com"
    assert extract_domain_from_url("http://example.org") == "example.org"
    assert extract_domain_from_url("https://my-site.co.in") == "my-site.co.in"

    # Invalid URL should return None
    assert extract_domain_from_url("not_a_url") is None
    assert extract_domain_from_url("ftp://example.com") is None
