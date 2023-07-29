#!/usr/bin/python3
"""
this module contain a class called Mylist
"""


class MyList(list):
    """
    this class contain a method print_sorted
    """
    pass

    def print_sorted(self):
        """
        this method sorted a list
        """

        print(sorted(list(self)))
