#!/usr/bin/python3
"""Module that returns dict desc for JSON serialization of obj"""


def class_to_json(obj):
    """Method to get dict description for JSON serialization of obj
        Args:
            obj: an instance of a Class
        Return:
            dict description
        """
    return obj.__dict__
