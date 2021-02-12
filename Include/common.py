""" Common module
implement commonly used functions here
"""

import random
import string


def generate_random(table):
    generated = ''
    last_value = table[-1]
    last_id = int(last_value[0])
    generated = str(last_id + 1)
    return generated


def create_dict(table):
    my_dict = {}
    for t in table:
        my_dict.setdefault(t[2], []).append(t[1:3])
    return my_dict
