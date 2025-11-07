import pytest

import sys


# Unconditional skip

@pytest.mark.skip(reason="This feature is deprecated")
def test_deprecated_feature():
    assert False


# Conditional skip based on Python version

@pytest.mark.skipif(

    sys.version_info < (3, 8),

    reason="Requires Python 3.8 or higher"

)
def test_python38_feature():
    # Uses features only available in Python 3.8+

    assert True


# Conditional skip based on platform

@pytest.mark.skipif(

    sys.platform != "linux",

    reason="Test only runs on Linux"

)
def test_linux_specific():
    assert True


# Skip during test execution

def some_condition():
    pass


def test_conditional_skip_inside_test():
    if some_condition():
        pytest.skip("Skipping due to condition")

    assert True


# Skip class entirely 

@pytest.mark.skip(reason="Entire class is skipped")
class TestSkippedClass:

    def test_one(self):
        assert False

    def test_two(self):
        assert False