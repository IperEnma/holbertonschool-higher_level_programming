#!/usr/bin/python3
import sys
if __name__ == "__main__":
    t = len(sys.argv)
    i = 1
    resultado = 0
    if (t == 2):
        print(f"{sys.argv[1]}")
    elif (t > 1):
        for x in range(1, t):
            resultado += int(sys.argv[i])
            i = i + 1
        print(f"{resultado}")
    else:
        print("0")
