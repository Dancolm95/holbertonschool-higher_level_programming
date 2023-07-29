#!/usr/bin/python3
"""
this module ocntain class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This cllss inherits from rectangle that inherits BaseGeometry
    """

    def __init__(self, size):
        """
        Method for initialized attributes
        """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Method return rectangle area
        """

        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
