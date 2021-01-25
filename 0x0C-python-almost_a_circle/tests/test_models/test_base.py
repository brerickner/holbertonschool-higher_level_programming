#!/usr/bin/python3
"""Module with unittest methods for base.py"""

import unittest
import pep8
from models.base import Base


class TestBaseClass(unittest.TestCase):

    """Class that contains unittest methods for base.py"""

    def setUp(self):
        """Method to assigning superclass private variable
           equal to zero before beginning testing"""
        Base._Base__nb_objects = 0

    def test_pep8_rec(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['models/base.py', 'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0, "pepfix Base")

    def test_id_mult_objs(self):
        """Method that tests mult obj id's created
           with different data types."""

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(-1)
        self.assertEqual(b2.id, -1)

        b3 = Base("")
        self.assertEqual(b3.id, "")

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base("meow")
        self.assertEqual(b5.id, "meow")

        b6 = Base("6.26")
        self.assertEqual(b6.id, "6.26")

        b7 = Base(None)
        self.assertEqual(b7.id, 2)

        b8 = Base(0)
        self.assertEqual(b8.id, 0)

    def test_one_id(self):
        """Method to test obj only"""
        obj = Base(-1)
        self.assertEqual(obj.id, -1)
