#!/usr/bin/python3
"""Module to unittest max int"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to unittest for max_integer([..])."""

    def test_empties(self):
        """Test an empty string."""
        self.assertIsNone(max_integer(""), None)

    def test_err_raises(self):
        """tests when errors should be raised"""
        self.assertRaises(Exception, max_integer, ["meow", "meow", 3])

    def test_for_realz(self):
        """tests that should find max int for real"""
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([221, 8, 77]),221)
        self.assertEqual(max_integer([-100, -99, -10]), -10)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([99, 99, 99, 98.5]), 99)


    