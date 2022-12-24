#!/usr/bin/python3
import sys
"""
Class that defines a square
"""


class Square:
    """
    defines square by private instance
    attribute - size
    """
    def __init__(self, size=0):
        """initialization of size attribute"""
        self.__size = size

    @property
    def size(self):
        """Getter-retrive size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size
        Raises TypeError if size is not int
        Raises ValueError if size is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns area of size"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with character # """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
