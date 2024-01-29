#!/usr/bin/python3
"""
Defines a class Rectangle

"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """it gets the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """it sets the private instance height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """gets the private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the private instace height"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """Public instance method area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """public instance method perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string
