#!/usr/bin/python3
"""Calculating the Area of a Square"""


class Square:
    """"
    defines a square based on private
    instance attribute and instation
    """
    def __init__(self, size=0):
        """ Initialization function"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates Area by multiplying size by itself"""
        return (self.__size * self.__size)
