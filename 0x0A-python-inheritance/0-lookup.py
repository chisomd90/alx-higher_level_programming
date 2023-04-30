#!/usr/bin/python3
# 0-lookup.py
"""This defines an object attribute lookup function."""


def lookup(obj):
    """This returns a list of an object's available attributes."""
    return (dir(obj))
