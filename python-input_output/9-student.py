#!/usr/bin/python3
"""
this module contain class Student
"""
class Student:
    """
    this class retrieves a dictionary representation of a student
    """

    def __init__(self, first_name, last_name, age):
        """
        this method initialized all attributes.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        thsi method retrieves a dictionary representation of a student
        instance.
        """

        return self.__dict__
