#!/usr/bin/python3
"""Module with unittest methods for rectangle.py"""

import unittest
import pep8
from models.rectangle import Rectangle
from models.base import Base
import re
import sys
import io
import contextlib


class TestRectangleClass(unittest.TestCase):

    """Class that contains unittest methods for Rectangle module"""

    def setUp(self):
        """Method to assigning superclass private variable
           equal to zero before beginning testing"""
        Base._Base__nb_objects = 0

    def test_pep8_rec(self):
        """Method to test pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['models/rectangle.py', 'tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0, "pepfix rectangle")

    def test_rectangle_id(self):
        """Method to test the id of Rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

        r4 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(r4.id, 0)

        r5 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r5.x, 0)
        self.assertEqual(r5.y, 0)
        self.assertEqual(r5.id, 12)

    def test_width_height_raises(self):
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

        with self.assertRaisesRegex(ValueError, htValErr):
            r1 = Rectangle(7, 0)

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

    def test_x_y_raises(self):
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

    def test_rec_attrs(self):
        """Method to test width and height of a Rectangle"""
        r1 = Rectangle(8, 8, 8, 8, 6)
        self.assertEqual(r1.width, 8)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 8)
        self.assertEqual(r1.y, 8)
        self.assertEqual(r1.id, 6)

    def test_area_rec(self):
        """Method to test area of Rectangle"""
        r1 = Rectangle(2, 10)
        self.assertEqual(r1.area(), 20)

        r1 = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r1.area(), 4)

    def test_str_method(self):
        """Method to test str representation of Rectangle"""

        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), '[Rectangle] (12) 2/1 - 4/6')

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), '[Rectangle] (1) 1/0 - 5/5')

        r3 = Rectangle(3, 3, 3, 3, 3)
        self.assertEqual(str(r3), '[Rectangle] (3) 3/3 - 3/3')

        r4 = Rectangle(3, 3, 3, 3)
        self.assertEqual(str(r4), '[Rectangle] (2) 3/3 - 3/3')

    def test_positional_args(self):
        """Method to test no-keyword and keyword arguments"""

        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), '[Rectangle] (1) 10/10 - 10/10')

        r1.update(89)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 10/10')

        r1.update(14, 2, 3)
        self.assertEqual(str(r1), '[Rectangle] (14) 10/10 - 2/3')

        r1.update(id=None)
        self.assertEqual(str(r1), '[Rectangle] (14) 10/10 - 2/3')

        r1.update(y=1, width=9, x=1, id=-89, height=9)
        self.assertEqual(str(r1), '[Rectangle] (-89) 1/1 - 9/9')

    def test_update_raises(self):
        """Method to test update method exception raises"""

        yValErr = "y must be >= 0"
        xValErr = "x must be >= 0"
        xTypeErr = "x must be an integer"
        yTypeErr = "y must be an integer"
        wdValErr = "width must be > 0"
        htValErr = "height must be > 0"
        wdTypeErr = "width must be an integer"
        htTypeErr = "height must be an integer"

        r1 = Rectangle(6, 2, 1, 8, 6)

        with self.assertRaisesRegex(ValueError, wdValErr):
            r1.update(6, 0, 1, 8, 6)

        with self.assertRaisesRegex(ValueError, htValErr):
            r1.update(6, 8, 0, 8, 6)

        with self.assertRaisesRegex(ValueError, xValErr):
            r1.update(8, 8, 7, -10, 7)

        with self.assertRaisesRegex(ValueError, yValErr):
            r1.update(8, 8, 7, 10, -7)

        with self.assertRaisesRegex(ValueError, yValErr):
            r1.update(y=-1, width=2, x=3, id=89)

        with self.assertRaisesRegex(ValueError, wdValErr):
            r1.update(y=1, width=0, x=3, id=89)

        with self.assertRaisesRegex(ValueError, xValErr):
            r1.update(y=1, width=9, x=-1, id=89)

        with self.assertRaisesRegex(ValueError, htValErr):
            r1.update(y=1, width=9, x=1, height=0)

        with self.assertRaisesRegex(TypeError, wdTypeErr):
            r1.update(y=1, width=None, x=1, id=-89, height=9)

    def test_display_raise(self):
        """Method to test display raises TypeError exception with 1 arg"""
        r0 = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaises(TypeError):
            r0.display(2)

    def test_display(self):
        """Method to test display output of square with # char"""

        r1 = Rectangle(2, 3, 0, 0)
        meow = "##\n##\n##\n"
        r1.display()
        assert re.match(r'^##\n##\n##\n$', meow)

        r1 = Rectangle(2, 3, 3, 0)
        meow = "   ##\n   ##\n   ##\n"
        assert re.match(r'^   ##\n   ##\n   ##\n$', meow)

        """output = sys.stdout
        r1 = Rectangle(3,2, 0, 0)
        """

        r1 = Rectangle(2, 3, x=0, y=0)
        outputStr = io.StringIO()
        with contextlib.redirect_stdout(outputStr):
            r1.display()
        self.assertEqual("##\n##\n##\n", outputStr.getvalue())

        """
        self.assertEqual(r1.display(), meow)
        suite = unittest.TestLoader().loadTestsFromModule(__Rectangle__)
        with io.StringIO() as buf:
            with contextlib.redirect_stdout(buf):
                unittest.TextTestRunner(stream=buf).run(suite)
        """

        r1 = Rectangle(2, 3, 1, 1)
        meow = "\n ##\n ##\n ##\n"
        outputStr = io.StringIO()
        with contextlib.redirect_stdout(outputStr):
            r1.display()
        self.assertEqual("\n ##\n ##\n ##\n", outputStr.getvalue())

        r2 = Rectangle(3, 2)
        outputStr = io.StringIO()
        with contextlib.redirect_stdout(outputStr):
            r2.display()
        self.assertEqual("###\n###\n", outputStr.getvalue())

        r2 = Rectangle(3, 2, 2)
        outputStr = io.StringIO()
        with contextlib.redirect_stdout(outputStr):
            r2.display()
        self.assertEqual("  ###\n  ###\n", outputStr.getvalue())

        r2 = Rectangle(3, 2, 2, 0)
        outputStr = io.StringIO()
        with contextlib.redirect_stdout(outputStr):
            r2.display()
        self.assertEqual("  ###\n  ###\n", outputStr.getvalue())

        r2 = Rectangle(3, 2, 0, 1, 1)
        outputStr = io.StringIO()
        with contextlib.redirect_stdout(outputStr):
            r2.display()
        self.assertEqual("\n###\n###\n", outputStr.getvalue())

        r2 = Rectangle(3, 2, 0, 0, 1)
        outputStr = io.StringIO()
        with contextlib.redirect_stdout(outputStr):
            r2.display()
        self.assertEqual("###\n###\n", outputStr.getvalue())

    def test_dict_repr(self):
        """Method to test dict repr of a Rectangle"""

        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        self.assertDictEqual(
            r1_dict, {'id': 1, 'x': 1, 'height': 2, 'y': 9, 'width': 10})

        r2 = Rectangle(1, 1)
        r2.update(**r1_dict)
        r2_dict = r2.to_dictionary()
        self.assertDictEqual(
            r2_dict, {'id': 1, 'x': 1, 'height': 2, 'y': 9, 'width': 10})

        r2.update(5, 5, 5, 5, 5)
        r2_dict = r2.to_dictionary()
        self.assertDictEqual(
            r2_dict, {'id': 5, 'x': 5, 'height': 5, 'y': 5, 'width': 5})

        r1 = Rectangle(1, 1, 2, 5, 6)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dict)
        r2_dict = r2.to_dictionary()
        self.assertDictEqual(
            r2_dict, {'id': 6, 'x': 2, 'height': 1, 'y': 5, 'width': 1})

    def test_instance_type(self):
        """Method to test types of single Rectangle obj"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        self.assertIs(type(r1), Rectangle)
        self.assertIs(type(r1_dict), dict)
        self.assertIsInstance(Rectangle(10, 2, 1, 9), Base)

    def test_instances_type(self):
        """Method to test types when more than one instance"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dict)
        self.assertIs(type(r1), Rectangle)
        self.assertIs(type(r1_dict), dict)
        self.assertIs(type(r2), Rectangle)
        self.assertIs(type(r1_dict), dict)
        self.assertNotEqual(r1, r2)
        self.assertIsNot(r1, r2)

    def test_instances_five_args(self):
        """Method to test instances type when 5 args given"""
        r1 = Rectangle(1, 1, 2, 5, 6)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dict)
        r2_dict = r2.to_dictionary()
        self.assertIs(type(r1), Rectangle)
        self.assertIs(type(r1_dict), dict)
        self.assertIs(type(r2), Rectangle)
        self.assertIs(type(r2_dict), dict)
        self.assertNotEqual(r1, r2)
        self.assertIsNot(r1, r2)
