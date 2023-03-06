#!/usr/bin/python3
# square.py
"""Define Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square: Class define square
    Args:
        Rectangle(Class): parent class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.siz = size

    def __str__(self):
        """
            __str__ print information for square

        returns:
            [str]: [Square] (<id>) <x>/<y> - <size>
        """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(self.id, self.x,
                self.y, self.width)

    @property
    def size(self):
        """Getter value for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter value for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update use args and kwargs"""
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))
    def to_dictionary(self):
        """
            returns the dictionary
            representation of a square
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
