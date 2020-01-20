#!/usr/bin/python3
""" Return a list object.
"""


def lookup(obj):
        """ Returns the list of available attributes and
            methods of an objec
        Args:
            obj: a object
            Return: a list object
        """
        return dir(obj)
