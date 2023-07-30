#!/usr/bin/python3
"""
this module contain class append_write
"""


def append_write(filename="", text=""):
    """
    Write a function that appends a string at the end of a text file
    and returns the number of characters added.
    """

    with open(filename, 'a') as f:
        return f.write(text)
