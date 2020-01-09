#!/usr/bin/python3
class Square():

    """ Square class with one priveteatribute"""

    def __init__(self, size=0):
        """ __init___ constructor of Square class

        Args:
            size (int): size of Square.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    def area(self):
    
        """ Calculate area of square
        return: area
        """

        return self.__size ** 2 
