#!/usr/bin/python3
""" Class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square inherits from Rectangle
    """
    def __init__(self, size):
        """ initialize size

        Args:
            size: size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)  # call init of rectangle class
        self.__size = size
