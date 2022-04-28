#!/usr/bin/python3
import sys
t = len(sys.argv)
i = 1
if (t == 1):
    print("0 arguments.")
else:
    print(f"{t - 1} argument:")
    for x in range(1,t):
        print(f"{i} = {sys.argv[i]}")
        i = i + 1
