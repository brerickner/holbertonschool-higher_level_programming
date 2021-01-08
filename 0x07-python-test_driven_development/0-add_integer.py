#!/usr/bin/python3
"""This is our adding module"""


def add_integer(a, b=98):
    """Method to add two integers.
        Args:
            a: integer
            b: integer
        Return:
            a + b
            """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")

    elif isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
