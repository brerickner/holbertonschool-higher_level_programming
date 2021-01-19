#!/usr/bin/python3
"""Module for class Mylist"""


class MyList(list):

    """Subclass inheriting from superclass list"""

    def __init__(self):
        """Instantiation of Mylist obj"""
            # self.__self = self

    def print_sorted(self):
        """Method to print sorted list of attr and methods from obj"""
        print(sorted(self))
