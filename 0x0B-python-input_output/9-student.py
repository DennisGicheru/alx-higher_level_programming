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

    def to_json(self):
        """retrieve dictionary representation
        of a student"""
        return (self.__dict__)
