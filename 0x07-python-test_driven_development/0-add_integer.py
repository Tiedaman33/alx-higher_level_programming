#!/usr/bin/python3
"""Defines an interger additon function."""


def add_integer(a, b=98):
    """Return the integer additon function of a and b.

    float arguments are typecasted to ints before addtion is performed.

    Raises:
        TypeError: if either of a or b is anon-integer and non-float.
        """
        if ((not isinstance(a, int) and not isinstance(a, float)):
                raise TypeError("a must be an integer")
        if ((not isinstance(a, int) and not isinstance(b, float)):
            raise TypeError("b must be an integer")
        return (int(a) + int(b))
