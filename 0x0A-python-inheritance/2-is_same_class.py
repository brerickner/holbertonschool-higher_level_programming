#!/usr/bin/python3
"""Module for is_same_class method"""


def is_same_class(obj, a_class):
    """Method that returns True when obj is exactly instance of class
        Args:
            obj: object to test if instance of class
            a_class: class to test if obj is instance of
        Return:
            True when obj is exactly instance of class. Else False.
        """
    if (isinstance(obj, a_class)) is False:
        return False
    return True
