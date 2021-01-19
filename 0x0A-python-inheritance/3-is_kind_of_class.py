#!/usr/bin/python3
"""Module for is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """ Method that returns True when obj is instance of class
        or obj is instance of class inherited from specific class.
        Args:
            obj: object to test if instance of class
            a_class: class to test if obj is instance of
        Return:
            True when obj is instance of class/inherited class.
            Else False.
        """
    if isinstance(obj, a_class) is False:
        return False
    return True
