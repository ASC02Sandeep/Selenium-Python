import pytest
import sys

# Expected to fail

@pytest.mark.xfail
def test_expected_to_fail():
    """This test is expected to fail"""

    assert False


# Expected to fail with condition

@pytest.mark.xfail(sys.platform == "win32", reason="Bug on Windows")
def test_windows_bug():
    assert False


# Expected to fail but passes (XPASS)

@pytest.mark.xfail
def test_unexpected_success():
    """This test is marked xfail but passes"""

    assert True


# Strict mode - unexpected passes become errors

@pytest.mark.xfail(strict=True)
def test_strict_xfail():
    """If this passes, it will raise an error"""

    assert False  # Must fail


# XFail with reason

@pytest.mark.xfail(reason="Known issue with floating point precision")
def test_floating_point_precision():
    result = 0.1 + 0.2

    assert result == 0.3  # This might fail due to floating point precision