#!/usr/bin/python3
"""
module with prototype def lookup(obj)
"""


def lookup(obj):
    """
    Function that returns atributes.

    Args:
        obj: object of any type

    Returns:
        list of avaliable attributes and methods
    """

    return dir(obj)
