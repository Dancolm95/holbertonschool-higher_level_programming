#!/usr/bin/python3
"""
this module contain class_to_json.
"""


def class_to_json(obj):
    """
    this function returns the dictionary descxription with simple
    data structure for json serialization of an object.
    """
    return obj.__dict__
