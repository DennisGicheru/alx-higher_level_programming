#!/usr/bin/python3
"""
define class student
that defines a student by
public instance attributes
"""


class Student():
    """
    attributes:
    @first_name - attribute 1
    @last_name - attribute 2
    @age: attribute 3
    """
    def __init__(self, first_name, last_name, age):
        """Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve dictionary representation
        of a student
        attrs: return attribute names if attrs is a
        list of strings else return all attributes
        """
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            """return key, value pair if attrs is alist of strings"""
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return (self.__dict__)
