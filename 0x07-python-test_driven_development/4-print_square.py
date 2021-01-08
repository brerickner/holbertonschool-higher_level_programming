#!/usr/bin/python3
"""A simple module that prints square with char #"""


def print_square(size):
    """method that prints area of square with # chars
        Args:
            size: size length of square
        Raises:
            TypeError: size not int or is float less than 0
            ValueError: size less than 0
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("{}".format('#' * size), end="")
        print()
