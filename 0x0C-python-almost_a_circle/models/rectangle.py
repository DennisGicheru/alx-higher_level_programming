#!/usr/bin/python3
# rectangle.py
"""Rectangle class-inherits from base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle: Class define Rectangle

    Args:
        Base(class): parent class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__initialized constuctor

        Args:
            width(int)
            height(int)
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id ([type], optional): Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter value for width"""
        return self.__width

    @property
    def height(self):
        """Getter value for height"""
        return self.__height

    @property
    def x(self):
        """Getter value for x"""
        return self.__x

    @property
    def y(self):
        """getter value for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """
        Attributes:
            Value(int): value to be assigned

        Raises:
            TypeError: value must be of type int
            ValueError: Value must be > 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Attributes:
            Value(int): value to be assigned

        Raises:
            TypeError: Value must be of type int
            ValueError: Value must be > 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, x):
        """Setter value for x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """setter value for y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
            Returns area value of rectangle
        """
        return self.height * self.width

    def display(self):
        """
            display: prints in stdout the rectangle instance \
            with the character #
        """
        for row in range(self, y):
            print("")

        for col in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """
            __str__ print information for rectangle
        Returns:
            [str]: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """
            Update multiple Arr of the retangle
        """
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
                i += 1
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))

    def to_dictionary(self):
        """
            returns the dictionary
            representation of a Rectangle
        """
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
