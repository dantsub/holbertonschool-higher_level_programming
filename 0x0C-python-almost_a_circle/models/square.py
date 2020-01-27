#!/usr/bin/python3
"""
Square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Inicialize of Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Get size """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update arguments of class """
        attrs = ["id", "size", "x", "y"]
        if args:
            [setattr(self, attrs[idx], arg) for idx, arg in enumerate(args)]
        else:
            [setattr(self, key, val) for key, val in kwargs.items()]

    def to_dictionary(self):
        """ return dictionary of class """
        attrs = ["id", "size", "x", "y"]
        return {key: getattr(self, key) for key in attrs}
