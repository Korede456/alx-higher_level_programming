#!/usr/bin/python3

"""
    A rectangle object
"""

from models.base import Base


class Rectangle(Base):
    """
        Rectangle child class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            initializer
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):  """width getter """
        return self.__width

    @width.setter """setter"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self): """ height getter """
        return self.__height

    @height.setter """height setter"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__width = value

    @property """x getter """
    def x(self):
        return self.__x

    @x.setter """x setter"""
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property """y getter """
    def y(self):
        return self.__y

    @y.setter """ y setter """
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ calculates the area of a rectangle """
        return (self.height * self.width)

    def display(self):
        """ it displays a rectangle using # """
        for item in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """ returns a string representation of the class """
        return (f"[Rectangle] ({id}) {x}/{y} - {width}/{height}")
