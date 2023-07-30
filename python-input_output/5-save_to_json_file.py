#!/usr/bin/python3
"""
this module contain class save_to_json_file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    this funcion write an object to a text file
    using json representation
    """

    with open(filename, 'w') as f:
        filename = f.write(json.dumps(my_obj))
    return filename
