#!/usr/bin/env python

"""
Helper tools
"""

import typing


def get_subclasses(baseclass) -> dict:
    "Returns dict of name: subclasses given a baseclass"
    return {cls.__name__: cls for cls in baseclass.__subclasses__()}


def is_float(string) -> bool:
    "Returns True if float, false otherwise"
    if string == "" or string == "-":
        return True
    try:
        float(string)
        return True
    except ValueError:
        return False


def str_to_float(string) -> typing.Optional[float]:
    "Returns float value, None if failure."
    try:
        return float(string)
    except ValueError:
        return None
