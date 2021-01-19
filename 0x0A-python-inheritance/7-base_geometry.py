#!/usr/bin/python3
"""Module defining BaseGeometry class"""


class BaseGeometry:

    """Defines class BaseGeometry"""

    def area(self):
        """Method to raise Eception when area() not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value"""
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
