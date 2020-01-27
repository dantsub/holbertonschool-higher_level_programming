#!/usr/bin/python3
"""
Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Inicialize of Rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 1:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ Get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 1:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ Get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ Get y """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ Return area of class """
        return self.__height * self.__width

    def display(self):
        """ Print of representation of class """
        if self.__y:
            [print() for i in range(self.__y)]
        [print('{}{}'.format(' ' * self.__x, '#' * self.__width))
         for i in range(self.__height)]

    def __str__(self):
        """ Return representation of class """
        string = "[{}] ({}) ".format(type(self).__name__, self.id)
        string += "{}/{} -".format(self.__x, self.__y)
        if type(self) == Rectangle:
            string += " {}/{}".format(self.__width, self.__height)
        else:
            string += " {}".format(self.__width)
        return string

    def update(self, *args, **kwargs):
        """ update arguments of class """
        if type(self) == Rectangle:
            attrs = ["id", "width", "height", "x", "y"]
        else:
            attrs = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for idx, arg in enumerate(args):
                if attrs[idx] == "id" and arg == None:
                    self.__init__(self.width, self.height, self.x, self.y)
                setattr(self, attrs[idx], arg)
        elif kwargs and len(kwargs) > 0:
            for key, val in kwargs.items():
                if key == "id" and val == None:
                    self.__init__(self.width, self.height, self.x, self.y)
                setattr(self, key, val)

    def to_dictionary(self):
        """ return dictionary of class """
        if type(self) == Rectangle:
            attrs = ["id", "width", "height", "x", "y"]
        else:
            attrs = ["id", "size", "x", "y"]
        return {key: getattr(self, key) for key in attrs}
