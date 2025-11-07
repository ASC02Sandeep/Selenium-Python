
import re

def is_valid_email(email: str) -> bool:
    """Validate basic email format."""
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email) is not None


def is_valid_phone(phone: str) -> bool:
    """Validate phone number formats (e.g., +91-9876543210 or 9876543210)."""
    pattern = r"^(\+\d{1,3}[- ]?)?\d{10}$"
    return re.match(pattern, phone) is not None


# def is_strong_password(password: str) -> bool:
#     """Check password strength rules:
#        - At least 10 characters
#        - One uppercase, one lowercase, one digit, one special char
#     """
#     pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10,}$"
#     return re.match(pattern, password) is not None

def is_strong_password(password: str) -> bool:

    pattern = (
        r"^(?![a-z]{5,})"              # Prevents patterns like 'short', 'abcdef', 'mypassword'
        r"(?=.*[a-z])"                 # At least 1 lowercase
        r"(?=.*[A-Z])"                 # At least 1 uppercase
        r"(?=.*\d)"                    # At least 1 digit
        r"(?=.*[@$!%*?&])"             # At least 1 special char
        r"[A-Za-z\d@$!%*?&]{8,}$"      # Allowed characters + length >= 8
    )
    return re.match(pattern, password) is not None




def extract_domain_from_url(url: str) -> str:
    """Extract domain name from a valid URL."""
    pattern = r"https?://(www\.)?([A-Za-z0-9.-]+)"
    match = re.match(pattern, url)
    return match.group(2) if match else None
