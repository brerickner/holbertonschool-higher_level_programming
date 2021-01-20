#!/usr/bin/python3
"""Module defining write_file method"""


def write_file(filename="", text=""):
    """Method that writes a string to txt file
        Args:
            filename: file to write to
            text: text to write
        Returns:
            number of chars written
        """
    with open("my_first_file.txt", 'w', encoding="utf-8") as f:
        numOfChars = f.write(text)
        return numOfChars
