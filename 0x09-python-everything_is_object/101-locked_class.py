#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instanciating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __alots__ = ["first_name"]
