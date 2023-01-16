#!/usr/bin/python3

"""create class"""


class BaseGeometry:
    """create public instance method"""
    def area(self):
        """raises exception with message,
        Area not implemented"""
        raise Exception("area() is not implemented")
