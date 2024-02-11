#!/usr/bin/python3
"""
    This is the base of all classes in this project
"""

class Base:
    """ base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes the properties """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
