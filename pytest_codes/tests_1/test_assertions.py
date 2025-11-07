def test_basic_assertions():
    # Equality

    assert 5 == 5

    assert "hello" != "world"

    # Comparison

    assert 10 > 5

    assert 3 <= 3

    assert 2 < 4

    # Membership

    assert 3 in [1, 2, 3]

    assert 4 not in [1, 2, 3]

    # Identity

    x = [1, 2, 3]

    y = x

    assert x is y

    assert [1, 2, 3] is not [1, 2, 3]  # Different objects

    # Type checking

    assert isinstance("hello", str)

    assert type(42) is int

    # Truthiness

    assert True

    assert not False

    assert 1  # Truthy

    assert not 0  # Falsy

    assert "hello"  # Truthypy

    assert not ""  # Falsy