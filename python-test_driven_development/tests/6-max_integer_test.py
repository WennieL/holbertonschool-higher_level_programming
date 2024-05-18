#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_regular_lists(self):
        self.assertEqual(max_integer([1, 2, 3, 4,]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4,]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, -4,]), 2)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_argument(self):
        self.assertEqual(max_integer([5]), 5)

    def test_same_elements(self):
        self.assertEqual(max_integer([1, 1, 1]), 1)

    def test_float_number(self):
        self.assertEqual(max_integer([1.3, 2.7, 3.0, 4.5,]), 4.5)

    def test_strings(self):
        self.assertEqual(max_integer(["hello", "world", "eveyone"]), "world")


if __name__ == "__main__":
    unittest.main()
