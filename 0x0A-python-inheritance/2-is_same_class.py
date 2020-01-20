#!/usr/bin/python3
""" Return True or False
"""


def is_same_class(obj, a_class):

        """ Returns True if the object is exactly an instance of the specified class
            Otherwise False
        Args:
            obj: a object
            a_class: class name.

            Return: True or False
        """
        return True if type(obj) == a_class else False
