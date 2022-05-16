#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except ZeroDivisionError:
        print("Exception: division by zero", file=sys.stderr)
        return None
    except IndexError:
        print("Exception: list index out of range", file=sys.stderr)
        return None
