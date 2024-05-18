#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_regular_lists(self):
        """Test a regular list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4,]), 4)

    def test_negative_numbers(self):
        """Test a list with negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4,]), -1)

    def test_mixed_numbers(self):
        """Test a list of mixed integers."""
        self.assertEqual(max_integer([-1, 2, -3, -4,]), 2)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_argument(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_same_elements(self):
        """Test a list with the same values."""
        self.assertEqual(max_integer([1, 1, 1]), 1)

    def test_float_number(self):
        """Test an ordered list of floats."""
        self.assertEqual(max_integer([1.3, 2.7, 3.0, 4.5,]), 4.5)

    def test_strings(self):
        """Test an ordered list of strings."""
        self.assertEqual(max_integer(["hello", "world", "eveyone"]), "world")


if __name__ == "__main__":
    unittest.main()
