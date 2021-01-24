#!/usr/bin/python3
"""Module with unittest methods for base.py"""

import unittest
import pep8
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):

    """Class that contains unittest methods for Rectangle module"""

    def setUp(self):
        """Method to assigning superclass private variable
           equal to zero before beginning testing"""
        Base._Base__nb_objects = 0

    def test_rectangle_id(self):
        """Method to test the id of Rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_width_height(self):
        """Method to raise exceptions for width/height"""
        wdValErr = "width must be > 0"
        htValErr = "height must be > 0"
        wdTypeErr = "width must be an integer"
        htTypeErr = "height must be an integer"

        with self.assertRaisesRegex(ValueError, wdValErr):
            r1 = Rectangle(-2, 2)

        with self.assertRaisesRegex(ValueError, wdValErr):
            r1 = Rectangle(0, 2)

        with self.assertRaisesRegex(ValueError, wdValErr):
            r1 = Rectangle(0, 0)

        with self.assertRaisesRegex(ValueError, htValErr):
            r1 = Rectangle(7, -1)

        with self.assertRaisesRegex(TypeError, wdTypeErr):
            r1 = Rectangle(None, None)

        with self.assertRaisesRegex(TypeError, wdTypeErr):
            r1 = Rectangle(None, 10)

        with self.assertRaisesRegex(TypeError, htTypeErr):
            r1 = Rectangle(4, None)

        with self.assertRaisesRegex(TypeError, htTypeErr):
            r1 = Rectangle(1, 10.00000000000000000)

        with self.assertRaisesRegex(TypeError, htTypeErr):
            r1 = Rectangle(1, -1.0)

        with self.assertRaisesRegex(TypeError, wdTypeErr):
            r1 = Rectangle('x', 3)

        with self.assertRaisesRegex(ValueError, wdValErr):
            r2 = Rectangle(-5, 5, 1)

    def test_area_rec(self):
        """Method to test area of Rectangle"""
        r1 = Rectangle(2, 10)
        self.assertEqual(r1.area(), 20)

    def test_x_y(self):
        """Method to test cases involving x, y coordinates"""

        yValErr = "y must be >= 0"
        xValErr = "x must be >= 0"
        xTypeErr = "x must be an integer"
        yTypeErr = "y must be an integer"

        with self.assertRaisesRegex(TypeError, xTypeErr):
            r1 = Rectangle(3, 3, None, None)

        with self.assertRaisesRegex(ValueError, xValErr):
            r1 = Rectangle(3, 3, -1, 1)

        with self.assertRaisesRegex(ValueError, yValErr):
            r1 = Rectangle(3, 3, 1, -1)

        with self.assertRaisesRegex(TypeError, yTypeErr):
            r1 = Rectangle(3, 3, 3, None)

        with self.assertRaisesRegex(TypeError, xTypeErr):
            r1 = Rectangle(3, 3, None, 3)

    def test_pep8_rec(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['models/base.py', 'models/rectangle.py',
             'tests/test_models/test_rectangle.py',
             'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0, "Needs pepfixed")
        """
        with self.assertRaisesRegex(ValueError, wdTypeErr):
        with self.assertRaisesRegex(ValueError, wdTypeErr):

        """
