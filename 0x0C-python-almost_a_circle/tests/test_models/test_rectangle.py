#!/usr/bin/python3
"""Module with unittest methods for base.py"""

import unittest
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    """Class that contains unittest methods for Rectangle module"""
    
    def test_rectangle_id(self):
        """Method to test the id of Rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

"""Method to raise exceptions for width/height"""
    """r1 = Rectangle(-2, 2)
    ValueError: width must be > 0 

    r1 = Rectangle(0, 2)
    ValueError: width must be > 0

    r1 = Rectangle(0, 0)
    ValueError: width must be > 0 
    
    r1 = Rectangle(7, -1)
    ValueError: height must be > 0 
    
    r1 = Rectangle(None, None)
    TypeError: height must be an integer
    
    
    
    """




