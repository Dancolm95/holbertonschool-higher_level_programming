#!/usr/bin/python3
"""
this module ocntain class from_json_string
"""

import json


def from_json_string(my_str):
    """
    this class return an object represented by a json string
    """
    return json.loads(my_str)
