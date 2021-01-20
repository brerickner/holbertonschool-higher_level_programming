#!/usr/bin/python3
"""Module for inherits_from method"""


def inherits_from(obj, a_class):
    """ Method that returns True when obj is instance of class
        (directly, indirectly) inherited from specific class.
        Args:
            obj: object to test if instance of subclass
            a_class: class to test if obj is subclass instance of
        Return:
            True when obj is inherited instance of class
            (directly, indirectly). Else False.
        """
    if isinstance(obj, a_class) is False:
        return False
    elif type(obj) is a_class:
        return False
    return True
