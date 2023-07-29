#!/usr/bin/python3
"""
This module contain a method is_same_class
"""


def is_same_class(obj, a_class):
    """
    method return True if the object is an instance of the specified class
    """

    return type(obj) is a_class
