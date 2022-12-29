#!/usr/bin/python3
# 0-add_integer.py
"""
Simple function to add 2 integers
"""


def add_integer(a, b=98):
    """Returns the integer addition of a and b
    Float types have to be typecasted to int before addition
    raise type error if a or b is not int or float
    """
    if (a is None or not isinstance(a, int) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
