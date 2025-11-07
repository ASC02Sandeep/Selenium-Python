
from datetime import datetime, timedelta, timezone

def get_date_difference(date1: datetime, date2: datetime) -> int:
    """Return absolute difference in days between two dates."""
    return abs((date2 - date1).days)

def convert_to_timezone(dt: datetime, tz_offset_hours: int) -> datetime:
    """Convert a datetime to a specific timezone offset."""
    tz = timezone(timedelta(hours=tz_offset_hours))
    return dt.astimezone(tz)

def format_date(dt: datetime, fmt: str = "%Y-%m-%d") -> str:
    """Return date as formatted string."""
    return dt.strftime(fmt)

def calculate_age(birth_date: datetime, reference_date: datetime = None) -> int:
    """Calculate age in years given a birth date."""
    if reference_date is None:
        reference_date = datetime.now()
    years = reference_date.year - birth_date.year
    # Adjust if birthday hasn’t occurred yet this year
    if (reference_date.month, reference_date.day) < (birth_date.month, birth_date.day):
        years -= 1
    return years
