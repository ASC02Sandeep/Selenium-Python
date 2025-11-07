import unittest


def is_even(n):
    return n % 2 == 0


class TestSimple(unittest.TestCase):

    def test_is_even(self):
        self.assertTrue(is_even(2))

        self.assertFalse(is_even(3))


if __name__ == '__main__':
    unittest.main()