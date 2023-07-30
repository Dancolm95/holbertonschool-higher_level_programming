#!/usr/bin/python3
"""
this module contain function load_from_json_file
"""


import json


def load_from_json_file(filename):
    """
    function that creates an object from json file
    """
    with open(filename) as f:
        return json.loads(f.read())
