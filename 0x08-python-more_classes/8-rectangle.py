#!/usr/bin/python3
class Rectangle():
    """ Rectangle Class.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Init """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
                rec += str(self.print_symbol) * self.__width
                rec += "\n"
            rec = rec[:-1]
        return rec

    def __repr__(self):
        """ return string
        """
        return 'Rectangle(' + str(self.__width) + \
            ', ' + str(self.__height) + ')'

    def __del__(self):
        """ Delete instance
        """
        print("Bye rectangle...")
        if Rectangle.number_of_instances:
            Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Return bigger object
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
