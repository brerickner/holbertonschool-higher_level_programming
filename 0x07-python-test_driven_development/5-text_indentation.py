#!/usr/bin/python3
"""A module that prints 2 new lines after '.''?'':' in a text"""


def text_indentation(text):
    """Method that places 2 new lines after specified chars
        Args:
            text: text being modified
        Raises:
            TypeError: if text is not a string
            """
    newList = []
    replaceChar = ("\n" * 2)

    if isinstance(text, str) is False:
        TypeError("text must be a string")

    # if special char, and next char is space skip two chars then start string
    for char in range(len(text)):
        if text[char] is ":" or text[char] is "." or text[char] is "?":
            if text[:char + 1] is " " or "\n":

                text = text[:char + 1] + replaceChar + text[char + 2:]
                print(text, end="")
