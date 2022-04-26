#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        print("0", end="")
        return 0
    x = abs(number) % 10
    print("{}".format(x), end="")
    return x
