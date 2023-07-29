#!/usr/bin/python3
"""
this modle contin class BaseGeometry
"""


class BaseGeometry:
    """
    Basegeometry class
    """

    def area(self):
        """
        method calculated area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method for validate integers
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
