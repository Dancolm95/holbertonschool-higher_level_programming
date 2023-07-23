#!/usr/bin/python3
"""
    this module contain a Square class
"""

class Square:
    """class Square
        This class represent a Square.
    """

    def __init__(self, size=0):
        """__init__
            This method initialize the square.

            Attributes:
                size(int): The size of the square.

            Raises:
                TypeError: if size is not int.

                ValueError: if size is less than 0.

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """area
            Returns the square area.
        """
        return self.__size**2
