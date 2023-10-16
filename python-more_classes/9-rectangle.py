#!/usr/bin/python3
"""this is the first task, 1-rectangle
"""

class Rectangle:
    """The class only creates private instance attributes
       by taking in two arguments.

       Args:
            width (int): horizontal dimension of rectangle, default to 0
            height (int): vertical dimension of rectangle, default to 0
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns area of rectangle

        Attributes:
            width: horizontal dimension of rectangle
            height: vertical dimension of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """
        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += '#'
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """
        """
        return self._draw_rectangle()
    def __repr__(self):
        """
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
    @classmethod
    def __del__(cls):
        """
        """
        cls.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size
