#!/usr/bin/python3
for x in range(0, 100):
    print("{}".format(str(x).zfill(2)), end="")
    if x != 99:
        print(f", ", end="")
    if x == 99:
        print("")
