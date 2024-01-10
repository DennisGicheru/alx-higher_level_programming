#!/usr/bin/python3
"""
simple function that prints a text with 2 new lines
after certain characters are found
"""


def text_indentation(text):
    """
    prints two new lines after certain characters
    Args:
        text: the text or paragraph to be examined(must be str)
        first character .
        second character ?
        third character :
    each character to be replaced with two new lines
    Raise:
        TypeError: when text is not string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in text:
        a = ord(i)
        if a == 46 or a == 63 or a == 58:
            print(i)
            print()
        else:
            print(i, end="")
