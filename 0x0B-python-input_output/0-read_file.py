#!/usr/bin/python3
"""
a function that reads a text file
"""


def read_file(filename=""):
    """This reads a text file (UTF8) and prints it to stdout
    Returns none
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
