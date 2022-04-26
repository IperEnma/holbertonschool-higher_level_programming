#!/usr/bin/python3
for x in range(0, 100):
    if x < 99:
        print("{}, ".format(str(x).zfill(2)), end="")
    else:
        print("{}".format(str(x).zfill(2)))
