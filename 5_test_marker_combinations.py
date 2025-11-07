import time

import pytest


@pytest.mark.slow
@pytest.mark.integration
def test_slow_integration():
    """Slow integration test"""

    time.sleep(1)

    assert True


@pytest.mark.api
@pytest.mark.security
def test_secure_api():
    """Security test for API"""

    assert True


@pytest.mark.smoke
@pytest.mark.regression
def test_critical_functionality():
    """Critical smoke and regression test"""

    assert True