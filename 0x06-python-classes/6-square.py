#!/usr/bin/python3
class Square():

    """ Square class """

    def __init__(self, size=0, position=(0, 0)):
        """ __init___ constructor of Square class

        Args:
            size (int): size of Square.
            position (tuple): position of Square.
        """
        self.size = size
        self.position = position

    def area(self):

        """ Calculate area of square
        return: area
        """
        return self.__size ** 2

    def my_print(self):
        """ print a square
        """
        if self.__size:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print('{}{}'.format(' ' * self.position[0], '#' * self.__size))
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

    @property
    def position(self):

        """ Get method
        return: position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            if not isinstance(value[0], int) or not isinstance(value[1], int):
                if value[0] < 0 or value[1] < 0:
                    raise TypeError(
                        "position must be a tuple of 2 positive integers")
        self.__position = value
