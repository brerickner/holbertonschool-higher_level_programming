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
    
    for i in range(len(text)):
        if text[i] is ":":# or "." or "?":
            if text[i + 1] is " ":
                text = text[:i + 1] + replaceChar + text[i+2:]
                print(text)

   
            
            

            

