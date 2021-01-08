#!/usr/bin/python3
"""Module that prints first and last name"""

def say_my_name(first_name, last_name=""):
    """Method that prints first and last name
        Args:
            first_name: first name
            last_name: last name
        Raises:
            TypeError: when first and/or last name not string
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))