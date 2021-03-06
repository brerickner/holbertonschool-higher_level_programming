#!/usr/bin/python3
"""Module with unittest methods for base.py"""

import unittest
import os
import pep8
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):

    """Class that contains unittest methods for base.py"""

    def setUp(self):
        """Method to assigning superclass private variable
           equal to zero before beginning testing"""
        Base._Base__nb_objects = 0

    def test_pep8_rec(self):
        """Method to test pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['models/base.py', 'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0, "pepfix Base")

    def test_if_var_private(self):
        """Method to test if __nb_instances is private"""
        errB = "'Base' object has no attribute '_TestBaseClass__nb_instances'"
        with self.assertRaisesRegex(AttributeError, errB):
            b1 = Base().__nb_instances

    def test_id_mult_objs(self):
        """Method that tests mult obj id's created
           with different data types."""

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(-1)
        self.assertEqual(b2.id, -1)

        b3 = Base()
        self.assertEqual(b3.id, 2)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base("meow")
        self.assertEqual(b5.id, "meow")

        b6 = Base("6.26")
        self.assertEqual(b6.id, "6.26")

        b7 = Base(None)
        self.assertEqual(b7.id, 3)

        b8 = Base(0)
        self.assertEqual(b8.id, 0)

        b9 = Base(99)
        b9.id = 15
        self.assertEqual(b9.id, 15)

    def test_one_id(self):
        """Method to test one obj only"""
        obj = Base(-1)
        self.assertEqual(obj.id, -1)

        obj = Base(8)
        self.assertEqual(obj.id, 8)

        obj = Base(None)
        self.assertEqual(obj.id, 1)

        b1 = Base(float("nan"))
        self.assertIsNot(b1.id, float("nan"))

        b1 = Base('inf')
        self.assertIsNot(b1.id, float("nan"))

    def test_to_json(self):
        """Method to test JSON str representation of a dict"""
        r1_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_str = Base.to_json_string(r1_dict)
        test_dict = json.loads(json_str)

        self.assertEqual(test_dict, r1_dict)
        self.assertIs(type(json_str), str)
        self.assertIs(type(test_dict), dict)

    def test_to_json_with_to_dict(self):
        """Method to test JSON str representation of list_dictionaries"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_str = Base.to_json_string([dictionary])
        self.assertDictEqual(
            dictionary,
            {'width': 10,
             'y': 8,
             'x': 2,
             'id': 1,
             'height': 7})

        self.assertIs(type(dictionary), dict)
        self.assertIs(type(json_str), str)
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_create_method(self):
        """Method to test if classes dictionaries updated"""
        r1 = Rectangle(9, 9, 9, 9)
        s1 = Square(8, 8, 8, 8)
        r1_dict = r1.to_dictionary()
        s1_dict = s1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        s2 = Square.create(**s1_dict)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        s2 = Square.create(**s1_dict)

        self.assertEqual(str(r1), '[Rectangle] (1) 9/9 - 9/9')
        self.assertEqual(str(r2), '[Rectangle] (1) 9/9 - 9/9')
        self.assertNotEqual(r1, r2)
        self.assertIsNot(r1, r2)
        self.assertEqual(str(s1), '[Square] (8) 8/8 - 8')
        self.assertEqual(str(s2), '[Square] (8) 8/8 - 8')
        self.assertNotEqual(s1, s2)
        self.assertIsNot(s1, s2)

    def test_bens_apples(self):
        """Method to test create() with a peer's dictionary
        containing 5 apples"""
        better_dictionary = {
            'x': 4,
            'y': 4,
            'width': 4,
            'height': 4,
            'apples': 5,
            'id': 4,
            'x': 5,
            'y': 4,
            'width': 7}
        bens_test = Rectangle.create(**better_dictionary)
        self.assertEqual(str(bens_test), '[Rectangle] (4) 5/4 - 7/4')

    def test_load_file(self):
        """Method to test file loads Rectangle and Square"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        test = Rectangle.load_from_file()
        self.assertEqual([], test)

        test = Square.load_from_file()
        self.assertEqual([], test)

        r1 = Rectangle(6, 6, 6, 6)
        r2 = Rectangle(3, 3)
        passIn = [r1, r2]
        Rectangle.save_to_file(passIn)
        passOut = Rectangle.load_from_file()
        self.assertNotEqual(id(passIn[0]), id(passOut[0]))
        self.assertEqual(str(passIn[0]), str(passOut[0]))

        s1 = Square(6, 6, 6, 6)
        s2 = Square(3, 3)
        passIn = [s1, s2]
        Square.save_to_file(passIn)
        passOut = Square.load_from_file()
        self.assertNotEqual(id(passIn[0]), id(passOut[0]))
        self.assertEqual(str(passIn[0]), str(passOut[0]))

        """r1 = Rectangle(6, 6, 6, 6)
        r2 = Rectangle(3, 3,)
        passIn = [r2, r2]
        Rectangle.save_to_file()"""

        """def test_load_file(self):
        Module to test that Rectangles and Squares load from a file
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        testOut = Rectangle.load_from_file()
        self.assertEqual(str(testOut), str(test))
        """

    def test_to_save_sq(self):
        """Method to test files saved as squares for success and raises"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        with self.assertRaises(TypeError):
            Square.save_to_file()

        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

        Square.save_to_file([])
        with open("Square.json", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file([Square(1)])
        with open("Square.json", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), 38)

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_rect(self):
        """Method to test if files saved for rectangles"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 1)

        Rectangle.save_to_file([])
        with open("Rectangle.json", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), 2)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), 52)
