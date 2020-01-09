#!/usr/bin/python3
class Square():

    """ Square class with one priveteatribute"""

    def __init__(self, size=0):
        """ __init___ constructor of Square class

        Args:
            size (int): size of Square.
        """
        self.__size = size

    def area(self):

        """ Calculate area of square
        return: area
        """
        return self.__size ** 2

    def my_print(self):
        """ print a square
        """
        if self.__size:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()

    @property
    def size(self):

        """ Get method
        return: size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
