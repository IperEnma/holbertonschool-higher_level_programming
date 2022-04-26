#!/usr/bin/python3
def islower(c):
    asc = ord(c)
    if asc > 96 and asc < 123:
        return True
    else:
        return False
