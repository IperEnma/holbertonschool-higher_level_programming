#!/usr/bin/python3
import sys
if __name__ == "__main__":
    t = len(sys.argv)
    i = 1
    if (t == 1):
        print("0 arguments.")
    else:
        print(f"{t - 1} arguments:")
        for x in range(1, t):
            print(f"{i}: {sys.argv[i]}")
            i = i + 1
