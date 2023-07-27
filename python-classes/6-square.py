#!/usr/bin/python3
"""
    This module contains a class Square
"""


class Square:
    """ class Square
        This method represent a Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """__init__

            This method initialize a Square

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

        if self.__check_tuple(position) is False \
            or self.__check_indexes(position) is False \
            or self.__check_integers(position) is False \
            or self.__check_values(position) is False:
                raise TypeError('position must be a tuple of 2 positive integers')

        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if self.__check_tuple(position) is False \
            or self.__check_indexes(position) is False \
            or self.__check_integers(position) is False \
            or self.__check_values(position) is False:
                raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def __check_tuple(slef, position):
        if type(position) is tuple:
            return True

        return False

    def __check_indexes(self, position):
        if len(position) == 2:
            return True

        return False

    def __check_values(self, position):
        if position[0] >= 0 and position[1] >= 0:
            return True

        return False

    def area(self):
        """ area
            Return the square area.
        """
        return self.__size ** 2

    def my_print(self):
        if self.__size== 0:
            print()
            return None

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print('')

        for j in range(1, self.area() + 1):
            if j % self.__size == 1:
                print('{:>{w}}'.format('#', w=self.__position[0] + 1), end='')
            else:
                print('#', end='')

            if j % self.__size == 0 and j > 0:
                print()
