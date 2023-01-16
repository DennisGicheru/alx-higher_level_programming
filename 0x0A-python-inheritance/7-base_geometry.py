#!/usr/bin/python3

"""create class"""


class BaseGeometry:
    """create public instance method"""
    def area(self):
        """raises exception with message,
        Area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        Arguments:
          name {str} -- name of an instance
          value {int} -- type of instance
        Raises:
          TypeError: [must be an integer]
          ValueError:[must be greater than 0]
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
