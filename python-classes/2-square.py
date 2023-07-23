#!/usr/bin/python3
"""
    this module represent a class Square
"""


class Square:

    """
        This class represent a Square
    """

    def __init__(self, size=0):
        """__init__

            Este método inicializa el valor "size" del cuadrado.

            Attributes:
                size(int): The size of the square.

            Raises:
                TypeError: if 'size is not integer'.

                ValueError: if 'size is less than 0'.

        """

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
