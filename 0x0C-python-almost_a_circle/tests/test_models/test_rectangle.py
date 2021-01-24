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
    TypeError: width must be an integer

    r1 = Rectangle(2, 2)
    
    r4 = Rectangle(None, 10)
    print(r4.area())
    width must be an integer

    r4 = Rectangle(1.1, 10)
    print(r4.area())
    width must be an integer

    r4 = Rectangle(1, 10.00000000000000000)
    print(r4.area())
    TypeError: height must be an integer

    r4 = Rectangle(1, -1.0)
    print(r4.area())
    ValueError: height must be > 0 

    r4 = Rectangle('x', 3)
    print(r4.area())
    TypeError: width must be an integer

TESTS FOR X, Y
    r3 = Rectangle(3, 3, None, None)
    print(r2)
    TypeError: x must be an integer
    
    
    
    """




