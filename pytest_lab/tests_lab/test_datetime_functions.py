
import pytest
from datetime import datetime, timedelta, timezone
from pytest_lab.src_lab.datetime_utils import (
    get_date_difference,
    convert_to_timezone,
    format_date,
    calculate_age,
)

@pytest.mark.datetime
def test_date_comparisons_and_differences():
    """Verify date difference calculations."""
    d1 = datetime(2025, 1, 1)
    d2 = datetime(2025, 1, 10)

    assert get_date_difference(d1, d2) == 9
    assert get_date_difference(d2, d1) == 9  # order shouldn’t matter

@pytest.mark.datetime
def test_timezone_conversions():
    """Check timezone offset conversions."""
    dt = datetime(2025, 11, 4, 12, 0, tzinfo=timezone.utc)

    # Convert UTC → IST (UTC+5:30)
    converted = convert_to_timezone(dt, 5.5)
    assert converted.utcoffset().total_seconds() == 5.5 * 3600

    # Convert UTC → EST (UTC-5)
    converted2 = convert_to_timezone(dt, -5)
    assert converted2.utcoffset().total_seconds() == -5 * 3600

@pytest.mark.datetime
def test_date_formatting_strings():
    """Validate formatted date strings."""
    dt = datetime(2025, 11, 4, 15, 30)
    assert format_date(dt) == "2025-11-04"
    assert format_date(dt, "%d/%m/%Y") == "04/11/2025"
    assert "2025" in format_date(dt, "%Y-%m-%d %H:%M")

@pytest.mark.datetime
def test_age_calculation_validations():
    """Ensure correct age calculation logic."""
    birth_date = datetime(2000, 6, 15)
    reference_date = datetime(2025, 6, 14)
    assert calculate_age(birth_date, reference_date) == 24  # one day before birthday

    reference_date2 = datetime(2025, 6, 15)
    assert calculate_age(birth_date, reference_date2) == 25  # birthday reached

    # Age with current date (should be int)
    assert isinstance(calculate_age(birth_date), int)
