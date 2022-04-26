#!/usr/bin/python3
def islower(c):
    asc = ord(c)
    if asc > 96 and asc < 123:
        return True
    else:
        return False


def uppercase(str):
    for x in str:
        if islower(x):
            y = ord(x) - 32
            x = chr(y)
        print(f"{x}", end="")
    print("")
