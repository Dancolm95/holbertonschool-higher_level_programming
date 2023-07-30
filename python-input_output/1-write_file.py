#!/usr/bin/python3
"""
this module contain class write_files
"""


def write_file(filename="", text=""):
    """
    This class write files
    """

    with open(filename, 'w') as f:
        return f.write(text)
