#!/usr/bin/python3
"""A module that prints 2 new lines after '.''?'':' in a text2"""


def text_indentation(text):
    """Method that places 2 new lines after specified chars
        Args:
            text2: text2 being modified
        Raises:
            TypeError: if text2 is not a string
            """

    if isinstance(text, str) is False:
        TypeError("text must be a string")

    text2 = text.strip()

    # if special idx, and next idx is space skip two chars then start string
    for idx in range(len(text2)):
        print(text2[idx], end="")

        if text2[idx] is ":" or text2[idx] is "." or text2[idx] is "?":
            print("\n")
            if idx < len(text2) - 1 and text2[idx + 1] is " " or text2[idx + 1] is "\n":
                idx += 1
            idx += 1
