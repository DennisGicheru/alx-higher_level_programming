#!/usr/bin/python3
"""
Class Square that defiens a square
"""


class Square:
    """defines a square by private instance attribute
    Size must be of type int
    else error will be raised"""

    def __init__(self, size=0):
        """
        Initializes the square
        Returns None
        """
        self.__size = size

    @property
    def size(self):
        """Getter- returns size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter of size
        Raises TypeError if size is not int
        Raises ValueError is size is less than Zero
        """
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ calculates area by multiplying size by itself
        Returns int
        """
        return self.__size ** 2
