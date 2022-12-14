#!/usr/bin/python3

"""Class Rectangle that defines a rectangle"""


class Rectangle:
    """define __init__ to intialize"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initialize a new rectangle with 2
        parameters
        width: width of rectangle
        height: height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter-to retrieve"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gettter to retrieve"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculate area of rectangle
        Returns: int area
        """
        return (self.__height*self.__width)

    def perimeter(self):
        """calculates perimeter of rectangle
        Returns: int perimeteter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((2*self.__height) + (2*self.__width))

    def __str__(self):
        """prints rectangle using #
        use iteration to loop through height and width
        """
        if self.__height == 0 or self.__width == 0:
            return ""

        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            string = string + "\n"
        return (string[:-1])

    def __repr__(self):
        """string representation or value"""
        return "Rectangle(" + str(self.__width) + ', ' \
            + str(self.__height) + ")"

    def __del__(self):
        """prints message when instance
        is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
