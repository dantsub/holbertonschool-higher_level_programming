#!/usr/bin/python3
class Rectangle():
    """ Rectangle Class.
    """
    def __init__(self, width=0, height=0):
        """ Init """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Get width """
        return self.__width

    @property
    def height(self):
        """ Get height """
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Return area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """ Return perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ Return printable representation
        """
        rec = ""
        if self.__width > 0 and self.__height > 0:
            for idx in range(self.__height):
                rec += "#" * self.__width
                rec += "\n"
            rec = rec[:-1]
        return rec

    def __repr__(self):
        """ return string
        """
        return 'Rectangle(' + str(self.__width) + \
            ', ' + str(self.__height) + ')'
