#!/usr/bin/python3
"""Module defining read_file method"""


def read_file(filename=""):
    """Method that reads text file(UTF8) and prints to stdout
        Args:
            filename: file to read from
        """
    with open("my_file_0.txt", 'r') as f:
        print(f.read())
