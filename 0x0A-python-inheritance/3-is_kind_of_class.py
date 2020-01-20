#!/usr/bin/python3
""" Return True or False
"""


def is_kind_of_class(obj, a_class):
        """ Returns True if the object is an instance of,
            or if the object is an instance of a class that inherited from,
            the specified class, otherwise False.
        Args:
            obj: a object.
            a_class: a Class.
            Return: True or False.
        """
        return True if isinstance(obj, a_class) else False
