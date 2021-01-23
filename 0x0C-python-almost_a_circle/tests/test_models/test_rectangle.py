#!/usr/bin/python3
"""Module with unittest methods for base.py"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    """Class that contains unittest methods for Rectangle module"""\
    
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_rectangle_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
