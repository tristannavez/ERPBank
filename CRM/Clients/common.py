""" Common module
implement commonly used functions here
"""

import random
import string


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''
    minChar = 8
    maxChar = 8
    allChar = string.ascii_letters + string.punctuation + string.digits
    generated = "".join(random.choice(allChar) for x in range(random.randint(minChar, maxChar)))
    return generated


def create_dict(table):
    my_dict = {}
    for t in table:
        my_dict.setdefault(t[2], []).append(t[1:3])
    return my_dict
