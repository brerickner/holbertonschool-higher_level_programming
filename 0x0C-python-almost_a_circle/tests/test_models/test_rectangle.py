#!/usr/bin/python3
"""Module with unittest methods for base.py"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    """Class that contains unittest methods for Rectangle module"""\
    
    r1 = Rectangle(10, 2)
    self.assertEqual(r1.id, 1)
    