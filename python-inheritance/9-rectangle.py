#!/usr/bin/python3
"""
this module contain a class BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from baseGeometry
    """
    
    def __init__(self, width, height):
        """
        this method for initialized the attributes
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        This method define a area
        """

        return self.__width * self.__height

    def __str__(self):
        """
        this method for return the next string
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
