#!/usr/bin/python3

"""
class rectangle module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherits from BaseGeometry class"""
    def __init__(self, width, height):
        """instantiation of
        width and height
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Return statement with rectangle height and width"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))