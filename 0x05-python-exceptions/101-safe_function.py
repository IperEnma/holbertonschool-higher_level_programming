#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except ZeroDivisionError:
        print("Exception: division by zero")
        return None
    except IndexError:
        print("Exception: list index out of range")
        return None
