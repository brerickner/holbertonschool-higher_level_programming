#!/usr/bin/python3
"""Module defining append_write method"""


def append_write(filename="", text=""):
    """Method that appends a string to end txt file
        Args:
            filename: file to append to
            text: text to append
        Returns:
            number of chars added
        """
    with open(filename, 'a', encoding="utf-8") as f:
        charsAdded = f.write(text)
        return charsAdded
