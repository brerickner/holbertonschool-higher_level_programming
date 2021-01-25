#!/usr/bin/python3
"""Module with unittest methods for square.py"""

import unittest
import pep8
from models.base import Base
from models.square import Square


class TestSquareClass(unittest.TestCase):

    """Class that contains unittest methods for Square module"""

    def setUp(self):
        """Method to assigning superclass private variable
           equal to zero before beginning testing"""
        Base._Base__nb_objects = 0

    def test_pep8_rec(self):
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

        r3 = Square(10, 2, 0, 12)
        self.assertEqual(r3.id, 12)

        r4 = Square(10, 2, 0, 0)
        self.assertEqual(r4.id, 0)

    def test_simple_attr(self):
        """Method that tests for correct output of size, x, y"""
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


"""

*arg tests*
s1 = Square(5)
[Square] (1) 0/0 - 5

s1 = Square(10)
[Square] (10) 0/0 - 5

s1 = Square(1, 2)
[Square] (1) 0/0 - 2

s1.update(1, 2, 3)
[Square] (1) 0/0 - 2

s1.update(1, 2, 3, 4)
[Square] (1) 4/0 - 2

s1.update(x=12)
[Square] (1) 12/0 - 2

s1.update(size=7, y=1)
[Square] (1) 12/1 - 7

s1.update(size=7, id=89, y=1)
[Square] (89) 12/1 - 7

*dict tests*
s1 = Square(10, 2, 1)
s1_dictionary = s1.to_dictionary()

def test_instances_five_args(self):
        **Method to test instances type when 5 args given**
        r1 = Square(1, 1, 2, 5, 6)
        r1_dict = r1.to_dictionary()
        r2 = Square(1, 1)
        r2.update(**r1_dict)
        r2_dict = r2.to_dictionary()
        self.assertIs(type(r1), Square)
        self.assertIs(type(r1_dict), dict)
        self.assertIs(type(r2), Square)
        self.assertIs(type(r2_dict), dict)
        self.assertNotEqual(r1, r2)
        self.assertIsNot(r1, r2)

def test_instances_type(self):
    *Method to test types when more than one instance*
        r1 = S(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        r2 = Square(1, 1)
        r2.update(**r1_dict)
        self.assertIs(type(r1), Square)
        self.assertIs(type(r1_dict), dict)
        self.assertIs(type(r2), Square)
        self.assertIs(type(r1_dict), dict)
        self.assertNotEqual(r1, r2)
        self.assertIsNot(r1, r2)

def test_dict_repr(self):
    **Method to test dict repr of a Square**

        r1 = Square(, , , )
        r1_dict = r1.to_dictionary()
        self.assertDictEqual(
            r1_dict, {'id': , 'x': , 'y': , 'size': })

        r2 = Square(, )
        r2.update(**r1_dict)
        r2_dict = r2.to_dictionary()
        self.assertDictEqual(
            r2_dict, {'id': , 'x': , 'height': , 'y': , 'width': })

        r2.update(, , , )
        r2_dict = r2.to_dictionary()
        self.assertDictEqual(
            r2_dict, {'id': 5, 'x': 5, 'size': 5, 'y': 5})

        r1 = Square(, , , )
        r1_dict = r1.to_dictionary()
        r2 = Square(1, 1)
        r2.update(**r1_dict)
        r2_dict = r2.to_dictionary()
        self.assertDictEqual(
            r2_dict, {'id': , 'x': , 'y': , 'size':})


"""
