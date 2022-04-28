#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    save = dir(hidden_4)
    for x in save:
        if (x[0] != '_' and x[1] != '_'):
            print(f"{x}")
