#!/usr/bin/python3
"""
Base module
"""


class Base():
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize Base """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
