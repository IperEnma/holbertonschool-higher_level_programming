#!/usr/bin/python3
import sys
t = len(sys.argv)
i = 1
resultado = 0
if (t == 2):
    print(f"{sys.argv[1]}")
elif (t > 1):
    for x in (1, t):
        resultado += int(sys.argv[i])
    print(f"{resultado}")
else:
    print("0")
