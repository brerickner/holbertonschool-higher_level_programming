#!/usr/bin/python3
"""Module to lookup an objects attr and methods"""


def lookup(obj):
    """Method returning list of avail attr and methods of an obj"""
    return list(dir(obj))
