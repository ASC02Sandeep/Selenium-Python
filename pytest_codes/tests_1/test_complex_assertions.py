def test_list_operations():
    numbers = [1, 2, 3, 4, 5]

    # List comprehensions in assertions

    assert all(x > 0 for x in numbers)

    assert any(x % 2 == 0 for x in numbers)

    # List equality

    assert numbers == [1, 2, 3, 4, 5]

    assert numbers != [1, 2, 3]

    # List length

    assert len(numbers) == 5


def test_string_operations():
    text = "Hello World"

    assert text.startswith("Hello")

    assert text.endswith("World")

    assert "lo Wo" in text

    assert text.upper() == "HELLO WORLD"

    assert text.lower() == "hello world"


def test_dictionary_operations():
    person = {"name": "John", "age": 30, "city": "New York"}

    assert person["name"] == "John"

    assert "age" in person

    assert "country" not in person

    assert person.keys() == {"name", "age", "city"}

    assert person.values()