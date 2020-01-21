#!/usr/bin/python3
""" Class BaseGeometry
"""


class BaseGeometry():
    """ Class BaseGeometry """
    def area(self):
        """ Function area not implemented """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):

        """ Method that validates value.

        Args:
            name: string.
            value: value.

        raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 1:
            raise ValueError('{} must be greater than 0'.format(name))
