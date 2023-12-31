#!/usr/bin/python3
"""
This module contain class read_file.
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    """

    with open(filename) as f:
        text = f.read()
        print(text, end="")
