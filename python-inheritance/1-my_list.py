#!/usr/bin/python3
"""
Module that contains a class MyList

"""


class MyList(list):
    """
    Class with method print_sorted
    """
    pass

    def print_sorted(self):
        """
        Methot that sorted a list
        """

        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
