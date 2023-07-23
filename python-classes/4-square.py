#!/usr/bin/python3
"""
    This module contains a class Square
"""


class Square:
    """ class Square
        This method represent a Square
    """
    def __init__(self, size=0):
        """__init__
            This methos initialize a Square

            Attributes:
                size(int): The size of a Square

            Raises:
                TypeError: if size type is not a int.
                ValueError: if size is less than 0
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """ area
            this method returns the square area.
        """
        return self.__size ** 2
