#!/usr/bin/python3

"""
    A rectangle object
"""

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)  """Calls the parent class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):  """width getter """
        return self.__width

    @width.setter """setter"""
    def width(self, value):
        self.__width = value

    @property
    def height(self): """ height getter """
        return self.__height

    @height.setter """height setter"""
    def height(self, value):
        self.__height = value

    @property """x getter """
    def x(self):
        return self.__x

    @x.setter """x setter"""
    def x(self, value):
        self.__x = value

    @property """y getter """
    def y(self):
        return self.__y

    @y.setter """ y setter """
    def y(self, value):
        self.__y = value
