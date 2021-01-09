#!/usr/bin/python3
"""A module that prints 2 new lines after '.''?'':' in a text"""


def text_indentation(text):
    """Method that places 2 new lines after specified chars
        Args:
            text: text being modified
        Raises:
            TypeError: if text is not a string
            """
    nLine = ("\n" * 2)

    if isinstance(text, str) is False:
        TypeError("text must be a string")

    # if special idx, and next idx is space skip two chars then start string
    for idx in range(len(text)):
        if text[idx] is ":" or text[idx] is "." or text[idx] is "?":
            if idx < len(text) - 1 and (text[idx + 1]) is " ":
                text = text[:idx + 1] + nLine + text[idx + 2:]
            text = text[:idx + 1] + nLine + text[idx + 1:]

    print(text, end="")
