#!/usr/bin/python3
"""Module with unittest methods for square.py"""

import unittest
import pep8
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquareClass(unittest.TestCase):

    """Class that contains unittest methods for Square module"""

    def setUp(self):
        """Method to assigning superclass private variable
           equal to zero before beginning testing"""
        Base._Base__nb_objects = 0

    def test_pep8_rec(self):
        """Method to test pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['models/square.py', 'tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0, "Pepfix Square")

    def test_square_id(self):
        """Method to test the id of Square"""
        s1 = Square(10, 2)
        self.assertEqual(s1.id, 1)

        s2 = Square(2, 10)
        self.assertEqual(s2.id, 2)

        s3 = Square(10, 2, 0, 12)
        self.assertEqual(s3.id, 12)

        s4 = Square(10, 2, 0, 0)
        self.assertEqual(s4.id, 0)

    def test_simple_attr(self):
        """Method that tests for correct output of size, x, y"""
        s1 = Square(6, 6, 6, 66)
        self.assertEqual(s1.size, 6)
        self.assertEqual(s1.width, 6)
        self.assertEqual(s1.height, 6)
        self.assertEqual(s1.x, 6)
        self.assertEqual(s1.y, 6)
        self.assertEqual(s1.id, 66)

        s1 = Square(5)
        self.assertEqual(str(s1), '[Square] (1) 0/0 - 5')

        s1 = Square(10)
        self.assertEqual(str(s1), '[Square] (2) 0/0 - 10')

    def test_square_attr_raises(self):
        """Method to raise exceptions for width/height"""
        wdValErr = "width must be > 0"
        wdTypeErr = "width must be an integer"
        yValErr = "y must be >= 0"
        xValErr = "x must be >= 0"
        xTypeErr = "x must be an integer"
        yTypeErr = "y must be an integer"

        with self.assertRaisesRegex(ValueError, wdValErr):
            s1 = Square(-2, 2)

        with self.assertRaisesRegex(TypeError, xTypeErr):
            s1 = Square(6, 22222.0)

        with self.assertRaisesRegex(ValueError, xValErr):
            s1 = Square(7, -1)

        with self.assertRaisesRegex(TypeError, wdTypeErr):
            s1 = Square(None, None)

        with self.assertRaisesRegex(TypeError, xTypeErr):
            s1 = Square(8, None, 0)

        with self.assertRaisesRegex(TypeError, yTypeErr):
            s1 = Square(4, 0, None)

        with self.assertRaisesRegex(ValueError, yValErr):
            s1 = Square(1, 10, -1)

        with self.assertRaisesRegex(TypeError, wdTypeErr):
            s1 = Square('x', 3)

    def test_sq_area_rec(self):
        """Method to test area of Square"""
        s1 = Square(2)
        self.assertEqual(s1.area(), 4)

        s1 = Square(2, 2, 2, 66)
        self.assertEqual(s1.area(), 4)

    def test_str_method_sq(self):
        """Method to test str representation of Square"""

        s1 = Square(5)
        self.assertEqual(Square.__str__(s1), '[Square] (1) 0/0 - 5')

        s2 = Square(3, 1)
        self.assertEqual(str(s2), '[Square] (2) 1/0 - 3')

        s3 = Square(8, 7, 6)
        self.assertEqual(str(s3), '[Square] (3) 7/6 - 8')

        s4 = Square(3, 3, 3, 3)
        self.assertEqual(str(s4), '[Square] (3) 3/3 - 3')

    def test_args_kwargs(self):
        """Method to test positional keyword arguments of Square"""

        s1 = Square(10)
        self.assertEqual(str(s1), '[Square] (1) 0/0 - 10')

        s1.update(10, 5)
        self.assertEqual(str(s1), '[Square] (10) 0/0 - 5')

        s1.update(14, 2, 3)
        self.assertEqual(str(s1), '[Square] (14) 3/0 - 2')

        s1.update(id=None)
        self.assertEqual(str(s1), '[Square] (14) 3/0 - 2')

        s1.update(x=12)
        self.assertEqual(str(s1), '[Square] (14) 12/0 - 2')

        s1.update(height=7, y=1)
        self.assertEqual(str(s1), '[Square] (14) 12/1 - 2')

        s1.update(y=1, size=9, x=1, id=6)
        self.assertEqual(str(s1), '[Square] (6) 1/1 - 9')

    def test_dict_repr(self):
        """Method to test dict repr of a Square"""

        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        self.assertDictEqual(
            s1_dict, {'id': 1, 'x': 2, 'y': 1, 'size': 10})

    def test_dict_after_update(self):
        """Method that tests dict repr after updating Square"""

        s1 = Square(5, 5, 5, 5)
        s1.update(1, 1)
        s1_dict = s1.to_dictionary()
        self.assertDictEqual(
            s1_dict, {'id': 1, 'x': 5, 'y': 5, 'size': 1})

    def test_instance_type(self):
        """Method to test types of single Square obj"""
        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()

        self.assertIs(type(s1), Square)
        self.assertIs(type(s1_dict), dict)
        self.assertIsInstance(Square(10, 2, 1), Base)
        self.assertIsInstance(Square(10, 2, 1), Rectangle)

    def test_instances_type(self):
        """Method to test types when more than one instance"""
        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dict)
        s2_dict = s2.to_dictionary()

        self.assertIs(type(s1), Square)
        self.assertIs(type(s1_dict), dict)
        self.assertIs(type(s2), Square)
        self.assertIs(type(s1_dict), dict)
        self.assertNotEqual(s1, s2)
        self.assertIsNot(s1, s2)

    def test_instances_four_args(self):
        """Method to test instances type when 5 args given"""
        s1 = Square(1, 2, 5, 6)
        s1_dict = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dict)
        r2_dict = s2.to_dictionary()

        self.assertIs(type(s1), Square)
        self.assertIs(type(s1_dict), dict)
        self.assertIs(type(s2), Square)
        self.assertIs(type(r2_dict), dict)
        self.assertNotEqual(s1, s2)
        self.assertIsNot(s1, s2)
