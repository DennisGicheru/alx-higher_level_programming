#!/usr/bin/python3
"""
Function that prints a square with the character #
"""


def print_square(size):
    """
    Purpose: prints a square with the character #
    Args:
        size: size length of the square
        Must be an integer
        must be greater than 0
    Raise:
        TypeError: when size is not int.
        "size must be an integer"
        ValueError: when size is less than 0
        "size must be >= 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for j in range(size):
        for j in range(size):
            print("#", end="")
        print()
