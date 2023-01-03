#!/usr/bin/python3

"""
Empty class that defines a Rectangle
"""


class Rectangle: 
    """Define Height and width"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """criteria for width"""
    def width(self, value):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        return (width)

    """criteria for height"""
    def height(self, value):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        return (height)
