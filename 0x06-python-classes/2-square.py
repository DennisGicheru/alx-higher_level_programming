#!/usr/bin/python3
"""
defines square by private instance attribute
"""


class Square:
    """
    size must be of type int
    else it will raise error
    """
    def __init__(self, size=0):
        """
        conditional statements to confirm size
        is int and is not less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
