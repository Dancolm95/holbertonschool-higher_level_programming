#!/usr/bin/python3
"""
this module contain a class Square
"""

Rectangle = __import__('9-rectangle').Rectangle



class Square(Rectangle):
    """
    this class that inherits from Rectangle that inherits BaseGeometry
    """

    def __init__(self, size):
        """
        This method initialized the attributes
        """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        This mnethod return rectangle area 
        """

        return self.__size ** 2
